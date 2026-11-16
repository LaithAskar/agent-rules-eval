def line_total(price, qty):
    return price * qty


def subtotal(lines):
    return sum(line_total(price, qty) for price, qty in lines)


def tax(amount, rate):
    return round(amount * rate / 100, 2)


def grand_total(lines, rate):
    sub = subtotal(lines)
    return round(sub + tax(sub, rate / 100), 2)
