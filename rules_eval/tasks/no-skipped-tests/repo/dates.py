def days_in_month(year, month):
    table = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return table[month - 1]
