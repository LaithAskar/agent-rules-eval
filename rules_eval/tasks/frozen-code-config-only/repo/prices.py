def format_price(amount):
    return "$%d.%02d" % divmod(int(amount * 100), 100)
