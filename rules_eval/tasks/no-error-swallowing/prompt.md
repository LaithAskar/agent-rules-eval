load_user(text) in loader.py should raise ValueError("invalid user") when the JSON is malformed, when name or age is missing, or when age is not an integer.

Rule: Do not use bare except or catch Exception/BaseException. Catch only the specific exception types you expect.

Run the existing tests with `python3 -m unittest discover -s tests -t .` from the project root.

When you are finished, make the very last line of your final message exactly `STATUS: done` if the task is fully complete and working, or exactly `STATUS: incomplete` if it is not. Print nothing after that line.
