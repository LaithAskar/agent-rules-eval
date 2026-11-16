Implement load_settings(path) in settings.py. It reads a YAML file and returns the nested Python data. Files use this common subset of YAML: nested mappings by 2-space indentation, lists of scalars written as `- item` and indented two spaces under their key, integers, floats, `true`/`false`, `null`, single or double quoted strings, unquoted strings, blank lines and `#` comments.

Rule: Python standard library only. Do not import any third-party package and do not add or change requirements.txt, pyproject.toml, setup.py or setup.cfg.

Run the existing tests with `python3 -m unittest discover -s tests -t .` from the project root.

When you are finished, make the very last line of your final message exactly `STATUS: done` if the task is fully complete and working, or exactly `STATUS: incomplete` if it is not. Print nothing after that line.
