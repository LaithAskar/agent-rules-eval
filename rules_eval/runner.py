import argparse
import json
import os
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone

from rules_eval.check import evaluate, git

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TASKS_DIR = os.path.join(ROOT, "tasks")
AGENTS_FILE = os.path.join(ROOT, "rules_eval", "agents.json")


def load_task(tasks_dir, name):
    task_dir = os.path.join(tasks_dir, name)
    with open(os.path.join(task_dir, "task.json"), encoding="utf-8") as handle:
        task = json.load(handle)
    with open(os.path.join(task_dir, "prompt.md"), encoding="utf-8") as handle:
        prompt = handle.read()
    return task_dir, task, prompt


def list_tasks(tasks_dir):
    return sorted(name for name in os.listdir(tasks_dir) if os.path.isfile(os.path.join(tasks_dir, name, "task.json")))


def make_workdir(task_dir):
    workdir = tempfile.mkdtemp(prefix="rules-eval-")
    shutil.copytree(os.path.join(task_dir, "repo"), workdir, dirs_exist_ok=True)
    git(workdir, "init", "-q", "-b", "main")
    with open(os.path.join(workdir, ".git", "info", "exclude"), "w", encoding="utf-8") as handle:
        handle.write("__pycache__/\n*.pyc\n")
    git(workdir, "add", "-A")
    git(workdir, "-c", "user.name=rules-eval", "-c", "user.email=rules-eval@example.invalid", "-c", "commit.gpgsign=false", "commit", "-q", "-m", "snapshot")
    base = git(workdir, "rev-parse", "HEAD").decode().strip()
    return workdir, base


def agent_config(agent, override):
    with open(AGENTS_FILE, encoding="utf-8") as handle:
        configs = json.load(handle)
    if override:
        base = configs.get(agent, {"final": "stdout"})
        return {"command": shlex.split(override), "final": base["final"]}
    if agent not in configs:
        raise SystemExit("unknown agent %r; known: %s, replay" % (agent, ", ".join(sorted(configs))))
    return configs[agent]


def as_text(value):
    if isinstance(value, bytes):
        return value.decode(errors="replace")
    return value or ""


def run_agent(config, prompt, workdir, meta_dir):
    final_file = os.path.join(meta_dir, "final.txt")
    command = [part.replace("{workdir}", workdir).replace("{final_file}", final_file).replace("{prompt}", prompt) for part in config["command"]]
    stdin_text = None if any("{prompt}" in part for part in config["command"]) else prompt
    started = time.time()
    timed_out = False
    try:
        proc = subprocess.run(command, cwd=workdir, input=stdin_text, capture_output=True, text=True, timeout=config["timeout"])
        stdout, stderr, code = proc.stdout, proc.stderr, proc.returncode
    except subprocess.TimeoutExpired as exc:
        stdout = as_text(exc.stdout)
        stderr = as_text(exc.stderr)
        code = None
        timed_out = True
    except FileNotFoundError as exc:
        raise SystemExit("agent command not found: %s" % exc)
    final_text = stdout
    if config["final"] == "file" and os.path.exists(final_file):
        with open(final_file, encoding="utf-8", errors="replace") as handle:
            final_text = handle.read()
    return {
        "final_text": final_text,
        "transcript": stdout + "\n" + stderr,
        "exit_code": code,
        "timed_out": timed_out,
        "duration_s": round(time.time() - started, 1),
    }


def run_replay(workdir, diff_path, final_path):
    if diff_path and os.path.getsize(diff_path) > 0:
        proc = subprocess.run(["git", "apply", "--whitespace=nowarn", os.path.abspath(diff_path)], cwd=workdir, capture_output=True, text=True)
        if proc.returncode != 0:
            raise SystemExit("diff does not apply: %s" % proc.stderr)
    final_text = ""
    if final_path:
        with open(final_path, encoding="utf-8") as handle:
            final_text = handle.read()
    return {"final_text": final_text, "transcript": final_text, "exit_code": 0, "timed_out": False, "duration_s": 0.0}


def secrets_of(task):
    return [secret for spec in task["rules"] if spec["type"] == "no_secret_leak" for secret in spec["secrets"]]


def redact(text, secrets):
    for secret in secrets:
        text = text.replace(secret, "[REDACTED]")
    return text


def run_task(name, agent, tasks_dir=TASKS_DIR, results_dir=None, diff=None, final=None, agent_command=None, keep_workdir=False, timeout=1800):
    task_dir, task, prompt = load_task(tasks_dir, name)
    workdir, base = make_workdir(task_dir)
    meta_dir = tempfile.mkdtemp(prefix="rules-eval-meta-")
    try:
        if agent == "replay":
            outcome = run_replay(workdir, diff, final)
        else:
            outcome = run_agent(dict(agent_config(agent, agent_command), timeout=timeout), prompt, workdir, meta_dir)
        score = evaluate(task_dir, task, workdir, base, outcome["final_text"], outcome["transcript"])
        diff_text = git(workdir, "diff", "--cached", "--binary", "--no-renames", base).decode(errors="replace")
    finally:
        if keep_workdir:
            print("workdir kept at %s" % workdir, file=sys.stderr)
        else:
            shutil.rmtree(workdir, ignore_errors=True)
        shutil.rmtree(meta_dir, ignore_errors=True)
    secrets = secrets_of(task)
    result = {
        "task": name,
        "category": task["category"],
        "agent": agent,
        "finished_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "exit_code": outcome["exit_code"],
        "timed_out": outcome["timed_out"],
        "duration_s": outcome["duration_s"],
        **score,
        "final_message": redact(outcome["final_text"], secrets),
        "transcript": redact(outcome["transcript"], secrets),
        "diff": redact(diff_text, secrets),
    }
    if results_dir:
        os.makedirs(results_dir, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        path = os.path.join(results_dir, "%s__%s__%s.json" % (name, agent, stamp))
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(result, handle, indent=2)
            handle.write("\n")
        result["result_file"] = path
    return result


def summary(result):
    keys = ("task", "agent", "task_done", "rule_kept", "honest", "claimed_status", "exit_code", "timed_out", "duration_s", "result_file")
    out = {key: result.get(key) for key in keys}
    out["violations"] = [violation for rule in result["rules"] for violation in rule["violations"]]
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(prog="rules_eval")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--task")
    parser.add_argument("--agent", help="claude, codex, replay, or a name from rules_eval/agents.json")
    parser.add_argument("--diff", help="replay only: diff to apply to the snapshot")
    parser.add_argument("--final", help="replay only: file holding the fake final message")
    parser.add_argument("--agent-command", help="override the command template, e.g. 'claude -p --model sonnet'")
    parser.add_argument("--results-dir", default=os.path.join(ROOT, "results"))
    parser.add_argument("--tasks-dir", default=TASKS_DIR)
    parser.add_argument("--timeout", type=int, default=1800, help="seconds before the agent is killed")
    parser.add_argument("--keep-workdir", action="store_true")
    args = parser.parse_args(argv)
    if args.list:
        print("\n".join(list_tasks(args.tasks_dir)))
        return 0
    if not args.task or not args.agent:
        parser.error("--task and --agent are required")
    result = run_task(args.task, args.agent, args.tasks_dir, args.results_dir, args.diff, args.final, args.agent_command, args.keep_workdir, args.timeout)
    print(json.dumps(summary(result), indent=2))
    return 0
