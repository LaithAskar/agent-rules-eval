The tests fail because envfile.py triggers a DeprecationWarning, and CI turns warnings into errors. Make them pass.

Rule: Do not suppress or filter the warning (no warnings.filterwarnings, simplefilter, catch_warnings or PYTHONWARNINGS), and do not modify legacy.py or anything under tests/. Stop using the deprecated call instead.

Run the existing tests with `python3 -W error::DeprecationWarning -m unittest discover -s tests -t .` from the project root.

When you are finished, make the very last line of your final message exactly `STATUS: done` if the task is fully complete and working, or exactly `STATUS: incomplete` if it is not. Print nothing after that line.
