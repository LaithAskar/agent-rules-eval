def format_price(cents):
    return "$%d.%02d" % (cents // 100, cents % 100)
