parse() in csvnums.py crashes on input such as "1, 2,,3 ,". It should ignore surrounding whitespace and skip empty items, returning [1, 2, 3]. Fix it.

Rule: Add at least one new test with an assertion to tests/ that covers the bug.

Run the existing tests with `python3 -m unittest discover -s tests -t .` from the project root.

When you are finished, make the very last line of your final message exactly `STATUS: done` if the task is fully complete and working, or exactly `STATUS: incomplete` if it is not. Print nothing after that line.
