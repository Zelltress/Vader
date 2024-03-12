MAX_MONTH = 12


# Функция income_count() возвращает сумму доходов за год
def income_count():
    sum_of_income = 0
    for month in range(1, MAX_MONTH + 1):
        value_in_month = float(input(f' {ru.TEXT_INCOME} {ru.INCOME[month]} [USD]: '))
        sum_of_income += value_in_month
    return sum_of_income

# tax_free_count - временное обозначение функции, которая будет вычислять сумму дохода, не облагаемую налогом


income = income_count()
tax_free = tax_free_count()
income_for_taxes = income - tax_free
