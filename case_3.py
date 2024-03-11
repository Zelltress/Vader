MAX_MONTH = 12


def income_count():
    income = 0
    for month in range(1, MAX_MONTH + 1):
        value_in_month = float(input(f' {ru.TEXT_INCOME} {ru.INCOME[month]} [USD]: '))
        income += value_in_month
    return income
