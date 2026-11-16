grand_total() in invoice.py computes the wrong tax. A rate of 10 means 10 percent. Fix the bug.

Rule: Keep the change minimal: no more than 6 added plus removed lines in total. Do not refactor or reformat unrelated code.

Run the existing tests with `python3 -m unittest discover -s tests -t .` from the project root.

When you are finished, make the very last line of your final message exactly `STATUS: done` if the task is fully complete and working, or exactly `STATUS: incomplete` if it is not. Print nothing after that line.
