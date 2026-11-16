import glob
import json
import os

from rules_eval import runner

SET_ORDER = {"original": 0, "hard": 1}


def load_results(results_dirs):
    latest = {}
    for results_dir in results_dirs:
        for path in sorted(glob.glob(os.path.join(results_dir, "*.json"))):
            with open(path, encoding="utf-8") as handle:
                result = json.load(handle)
            latest[(result["task"], result["agent"])] = result
    return latest


def task_meta(task_dirs):
    meta = {}
    for tasks_dir in task_dirs:
        for name in runner.list_tasks(tasks_dir):
            with open(os.path.join(tasks_dir, name, "task.json"), encoding="utf-8") as handle:
                task = json.load(handle)
            meta[name] = {"set": task.get("set", "custom"), "feasible": task.get("feasible", True)}
    return meta


def mark(value):
    return "yes" if value else "NO"


def outcome(run):
    feasible = run.get("feasible", True)
    success = run.get("success")
    if success is None:
        success = run["task_done"] and run["rule_kept"] and run["honest"]
    return success, feasible


def render_set(title, tasks, agents, latest, meta):
    lines = ["### %s" % title, ""]
    lines += ["| Agent | Runs | Correct outcome | rule_kept | honest | task_done (feasible tasks) |", "| --- | --- | --- | --- | --- | --- |"]
    for agent in agents:
        runs = [latest[(task, agent)] for task in tasks if (task, agent) in latest]
        if not runs:
            continue
        feasible_runs = [run for run in runs if outcome(run)[1]]
        lines.append("| %s | %d | %d/%d | %d/%d | %d/%d | %d/%d |" % (
            agent, len(runs),
            sum(outcome(run)[0] for run in runs), len(runs),
            sum(run["rule_kept"] for run in runs), len(runs),
            sum(run["honest"] for run in runs), len(runs),
            sum(run["task_done"] for run in feasible_runs), len(feasible_runs),
        ))
    lines += ["", "| Task | Kind | " + " | ".join("%s done / rule / honest" % agent for agent in agents) + " |", "| --- | --- |" + " --- |" * len(agents)]
    for task in tasks:
        cells = []
        for agent in agents:
            run = latest.get((task, agent))
            cells.append("-" if run is None else "%s / %s / %s" % (mark(run["task_done"]), mark(run["rule_kept"]), mark(run["honest"])))
        kind = "feasible" if meta.get(task, {}).get("feasible", True) else "impossible under rules"
        lines.append("| %s | %s | %s |" % (task, kind, " | ".join(cells)))
    return lines


def render(latest, meta):
    agents = sorted({agent for _, agent in latest})
    grouped = {}
    for task, _ in latest:
        label = latest[(task, next(a for a in agents if (task, a) in latest))].get("set") or meta.get(task, {}).get("set", "custom")
        grouped.setdefault(label, set()).add(task)
    lines = []
    for label in sorted(grouped, key=lambda item: (SET_ORDER.get(item, 99), item)):
        lines += render_set("%s tasks" % label, sorted(grouped[label]), agents, latest, meta) + [""]
    return "\n".join(lines)


def main(args):
    task_dirs = args.tasks_dir or runner.default_task_dirs()
    latest = load_results(args.results_dir)
    if not latest:
        raise SystemExit("no result files found in %s" % ", ".join(args.results_dir))
    text = render(latest, task_meta(task_dirs))
    if args.out:
        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write(text)
    else:
        print(text, end="")
    return 0
