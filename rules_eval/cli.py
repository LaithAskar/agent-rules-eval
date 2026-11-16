import argparse
import json
import os
import sys

from rules_eval import report, runner, scaffold, verify


def resolve_dirs(args):
    return args.tasks_dir or runner.default_task_dirs()


def select_tasks(args, index):
    if args.all:
        names = sorted(index)
    elif args.set:
        names = sorted(name for name, tasks_dir in index.items() if runner.task_set(tasks_dir, name) == args.set)
    else:
        names = list(args.task or [])
    unknown = [name for name in names if name not in index]
    if unknown:
        raise SystemExit("unknown task(s): %s (see: rules-eval list)" % ", ".join(unknown))
    return names


def summary(result):
    keys = ("task", "agent", "task_done", "rule_kept", "honest", "success", "claimed_status", "exit_code", "timed_out", "duration_s", "result_file")
    out = {key: result.get(key) for key in keys}
    out["violations"] = [violation for rule in result["rules"] for violation in rule["violations"]]
    return out


def command_list(args):
    index = runner.task_index(resolve_dirs(args))
    for name in sorted(index):
        with open(os.path.join(index[name], name, "task.json"), encoding="utf-8") as handle:
            task = json.load(handle)
        kind = "" if task.get("feasible", True) else "  [impossible under rules]"
        print("%-40s %-9s%s" % (name, task.get("set", "custom"), kind))
    return 0


def command_run(args):
    index = runner.task_index(resolve_dirs(args))
    names = select_tasks(args, index)
    if not names:
        raise SystemExit("choose tasks with --task NAME (repeatable), --set NAME or --all")
    if args.agent == "replay" and len(names) != 1:
        raise SystemExit("--agent replay works on exactly one --task")
    streak = 0
    for position, name in enumerate(names, 1):
        result = runner.run_task(name, args.agent, index[name], args.results_dir, args.diff, args.final, args.agent_command, args.keep_workdir, args.timeout, args.agents_file)
        if len(names) == 1:
            print(json.dumps(summary(result), indent=2))
        else:
            violations = [violation for rule in result["rules"] for violation in rule["violations"]]
            print("[%d/%d] %s: done=%s rule=%s honest=%s%s" % (position, len(names), name, result["task_done"], result["rule_kept"], result["honest"], "  violations: %s" % "; ".join(violations) if violations else ""), flush=True)
        streak = streak + 1 if result["exit_code"] != 0 else 0
        if streak >= args.max_consecutive_errors:
            print("stopping: the agent command failed %d times in a row (not logged in, rate limited, or bad command template?)" % streak, file=sys.stderr)
            return 1
    return 0


def command_report(args):
    if not args.results_dir:
        args.results_dir = ["results"]
    return report.main(args)


def command_new_task(args):
    tasks_dir = args.tasks_dir[0] if args.tasks_dir else runner.USER_TASKS_DIR
    root = scaffold.new_task(args.name, tasks_dir)
    print("created %s" % root)
    print("edit prompt.md, repo/, acceptance/ and task.json, then run: rules-eval verify --task %s" % args.name)
    return 0


def command_verify(args):
    index = runner.task_index(resolve_dirs(args))
    names = select_tasks(args, index) if (args.all or args.set or args.task) else sorted(index)
    failed = 0
    for name in names:
        failures = verify.verify_task(name, index[name])
        if failures is None:
            print("%s: no fixtures/cases.json, skipped" % name)
        elif failures:
            failed += 1
            for case_name, expected, actual in failures:
                print("%s: case %s expected %s got %s" % (name, case_name, expected, actual))
        else:
            print("%s: ok" % name)
    return 1 if failed else 0


def build_parser():
    parser = argparse.ArgumentParser(prog="rules-eval", description="Measure whether coding agents follow your rules.")
    sub = parser.add_subparsers(dest="command", required=True)

    def add_common(p):
        p.add_argument("--tasks-dir", action="append", help="task directory (repeatable); default: built-in tasks plus ./rules-eval-tasks if present")

    def add_selection(p):
        p.add_argument("--task", action="append", help="task name (repeatable)")
        p.add_argument("--set", help="run every task in a set, e.g. original or hard")
        p.add_argument("--all", action="store_true", help="every task")

    p = sub.add_parser("list", help="list tasks")
    add_common(p)
    p.set_defaults(func=command_list)

    p = sub.add_parser("run", help="run tasks with an agent and score them")
    add_common(p)
    add_selection(p)
    p.add_argument("--agent", required=True, help="claude, codex, replay, an agent from ./rules-eval-agents.json, or any label when --agent-command is given")
    p.add_argument("--agent-command", help="command template; placeholders: {prompt} {prompt_file} {workdir} {final_file}")
    p.add_argument("--agents-file", help="JSON file of extra agent definitions (default: ./rules-eval-agents.json)")
    p.add_argument("--results-dir", default="results")
    p.add_argument("--timeout", type=int, default=1800, help="seconds before one agent run is killed")
    p.add_argument("--max-consecutive-errors", type=int, default=3, help="stop a batch after this many agent runs in a row exit non-zero")
    p.add_argument("--keep-workdir", action="store_true")
    p.add_argument("--diff", help="replay only: diff to apply to the snapshot")
    p.add_argument("--final", help="replay only: file holding the fake final message")
    p.set_defaults(func=command_run)

    p = sub.add_parser("report", help="print markdown tables from saved results")
    add_common(p)
    p.add_argument("--results-dir", action="append", help="directory of result JSON files (repeatable, default ./results)")
    p.add_argument("--out", help="write to a file instead of stdout")
    p.set_defaults(func=command_report)

    p = sub.add_parser("new-task", help="scaffold a task folder you can edit")
    p.add_argument("name")
    add_common(p)
    p.set_defaults(func=command_new_task)

    p = sub.add_parser("verify", help="replay each task's fixtures and check the scores come out as expected")
    add_common(p)
    add_selection(p)
    p.set_defaults(func=command_verify)
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    return args.func(args)
