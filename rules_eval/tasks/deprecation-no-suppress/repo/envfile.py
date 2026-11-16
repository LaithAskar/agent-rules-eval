from legacy import parse_pair


def parse_env(text):
    values = {}
    for line in text.splitlines():
        if line.strip():
            key, value = parse_pair(line)
            values[key] = value
    return values
