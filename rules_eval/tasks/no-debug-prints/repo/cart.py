def total(prices, discount=0.0):
    subtotal = sum(prices)
    after = subtotal * (1 - discount)
    return round(after * (1 - discount), 2)
