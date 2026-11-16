import argparse
import glob
import json
import os

from rules_eval.runner import ROOT


def load(results_dir):
    latest = {}
    for path in sorted(glob.glob(os.path.join(results_dir, "*.json"))):
        with open(path, encoding="utf-8") as handle:
            result = json.load(handle)
        latest[(result["task"], result["agent"])] = result
    return latest


def mark(value):
    return "yes" if value else "NO"


def render(latest):
    agents = sorted({agent for _, agent in latest})
    tasks = sorted({task for task, _ in latest})
    lines = ["| Agent | Runs | task_done | rule_kept | honest |", "| --- | --- | --- | --- | --- |"]
    for agent in agents:
        runs = [latest[(task, agent)] for task in tasks if (task, agent) in latest]
        count = len(runs)
        lines.append("| %s | %d | %d/%d | %d/%d | %d/%d |" % (agent, count, sum(r["task_done"] for r in runs), count, sum(r["rule_kept"] for r in runs), count, sum(r["honest"] for r in runs), count))
    header = "| Task | " + " | ".join("%s done / rule / honest" % agent for agent in agents) + " |"
    lines += ["", header, "| --- |" + " --- |" * len(agents)]
    for task in tasks:
        cells = []
        for agent in agents:
            run = latest.get((task, agent))
            cells.append("-" if run is None else "%s / %s / %s" % (mark(run["task_done"]), mark(run["rule_kept"]), mark(run["honest"])))
        lines.append("| %s | %s |" % (task, " | ".join(cells)))
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(prog="rules_eval.summarize")
    parser.add_argument("--results-dir", default=os.path.join(ROOT, "results", "pass1"))
    args = parser.parse_args(argv)
    print(render(load(args.results_dir)), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
