import warnings


def parse_pair(text):
    warnings.warn("parse_pair is deprecated, use pairs.split_pair", DeprecationWarning, stacklevel=2)
    left, right = text.split("=")
    return left, right
