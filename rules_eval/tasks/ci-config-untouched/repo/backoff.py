def delay(attempt, base=1.0, cap=30.0):
    return base * 2 ** attempt
