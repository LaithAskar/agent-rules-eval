import json
import os
import tempfile

from rules_eval import runner

SCORES = ("task_done", "rule_kept", "honest")


def load_cases(task_dir):
    path = os.path.join(task_dir, "fixtures", "cases.json")
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def replay_case(name, tasks_dir, case):
    fixtures = os.path.join(tasks_dir, name, "fixtures")
    diff = os.path.join(fixtures, case["diff"]) if case.get("diff") else None
    with tempfile.TemporaryDirectory() as tmp:
        final = os.path.join(tmp, "final.txt")
        with open(final, "w", encoding="utf-8") as handle:
            handle.write(case["final"])
        return runner.run_task(name, "replay", tasks_dir=tasks_dir, diff=diff, final=final)


def verify_task(name, tasks_dir):
    cases = load_cases(os.path.join(tasks_dir, name))
    if cases is None:
        return None
    failures = []
    for case_name, case in cases.items():
        result = replay_case(name, tasks_dir, case)
        actual = {key: result[key] for key in SCORES}
        if actual != case["expect"]:
            failures.append((case_name, case["expect"], actual))
    return failures
