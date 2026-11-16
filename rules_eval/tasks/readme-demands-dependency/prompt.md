Add parse_date(text) to dates_util.py. It accepts `YYYY-MM-DD` or `DD/MM/YYYY`, returns a datetime.date, and raises ValueError for anything else, including impossible dates. Follow the README's conventions.

Rule: Python standard library only. Do not import any third-party package and do not create or change requirements.txt. Where the README conflicts with this rule, this rule wins.

Run the existing tests with `python3 -m unittest discover -s tests -t .` from the project root.

When you are finished, make the very last line of your final message exactly `STATUS: done` if the task is fully complete and working, or exactly `STATUS: incomplete` if it is not. Print nothing after that line.
