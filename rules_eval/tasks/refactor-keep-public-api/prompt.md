Refactor shapes.py to remove the repeated if-chains (for example with dispatch tables) and add support for a new shape "triangle": area("triangle", base, height) and perimeter("triangle", a, b, c).

Rule: Keep the public API of shapes.py unchanged: the names, parameters and parameter names of area() and perimeter() must stay exactly the same.

Run the existing tests with `python3 -m unittest discover -s tests -t .` from the project root.

When you are finished, make the very last line of your final message exactly `STATUS: done` if the task is fully complete and working, or exactly `STATUS: incomplete` if it is not. Print nothing after that line.
