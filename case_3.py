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

taxes_percent = [0, .1, .15, .25, .28, .33, .35, .396]
brackets_for_couple = [0, 18150, 73800, 148850, 226850, 405100, 457600]


def tax_for_married_couple(taxable_money):
    couple_tax = 0
    left_money = taxable_money
    for i in range(1, len(brackets_for_couple)):
        if taxable_money > brackets_for_couple[i]:
            couple_tax += (brackets_for_couple[i]-brackets_for_couple[i-1])*taxes_percent[i]
            left_money -= brackets_for_couple[i]-brackets_for_couple[i-1]
        else:
            couple_tax += left_money*taxes_percent[i]
            break
    return couple_tax
