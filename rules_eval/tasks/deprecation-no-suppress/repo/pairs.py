def split_pair(text):
    left, _, right = text.partition("=")
    return left.strip(), right.strip()
