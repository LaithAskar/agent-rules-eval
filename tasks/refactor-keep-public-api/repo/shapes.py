import math


def area(kind, *dims):
    if kind == "circle":
        return math.pi * dims[0] ** 2
    if kind == "rect":
        return dims[0] * dims[1]
    if kind == "square":
        return dims[0] * dims[0]
    raise ValueError(kind)


def perimeter(kind, *dims):
    if kind == "circle":
        return 2 * math.pi * dims[0]
    if kind == "rect":
        return 2 * (dims[0] + dims[1])
    if kind == "square":
        return 4 * dims[0]
    raise ValueError(kind)
