cast = int(input())

MAX_MONTH = 12

taxes_percent = [0, .1, .15, .25, .28, .33, .35, .396]
brackets_for_couple = [0, 18150, 73800, 148850, 226850, 405100, 457600]
brackets_for_subject = [0, 9075, 36900, 89350, 186350, 405100, 406750]


# Функция income_count() возвращает сумму доходов за год
def income_count():
    sum_of_income = 0
    for month in range(1, MAX_MONTH + 1):
        value_in_month = float(input(f' {ru.TEXT_INCOME} {ru.INCOME[month]} [USD]: '))
        sum_of_income += value_in_month
    return sum_of_income


# tax_free_count - временное обозначение функции, которая будет вычислять сумму дохода, не облагаемую налогом
def tax_free_count():
    amount = 0
    for month in range(1, MAX_MONTH + 1):
        free_amnt_mnth = float(input(f' {ru.FREE_TAX} {ru.INCOME[month]} [USD]: '))
        amount += free_amnt_mnth
    return amount


# Функция tax_for_married_couple(taxable_money) определяет величину годового налога на супружескую пару
def tax_for_married_couple(taxable_money):
    couple_tax = 0
    left_money = taxable_money
    for i in range(1, len(brackets_for_couple)):
        if taxable_money > brackets_for_couple[i]:
            couple_tax += (brackets_for_couple[i] - brackets_for_couple[i - 1]) * taxes_percent[i]
            left_money -= brackets_for_couple[i] - brackets_for_couple[i - 1]
        else:
            couple_tax += left_money * taxes_percent[i]
            break
    return couple_tax


# Функция определяет величину годового налога на субъект
def tax_for_subject(taxable_money):
    subject_tax = 0
    leftover = taxable_money
    for j in range(1, len(brackets_for_subject)):
        if taxable_money > brackets_for_subject[j]:
            subject_tax += (brackets_for_subject[j] - brackets_for_subject[j - 1]) * taxes_percent[j]
            leftover -= brackets_for_subject[j] - brackets_for_subject[j - 1]
        else:
            subject_tax += leftover * taxes_percent[j]
            break
    return subject_tax


def main():
    income = income_count() - tax_free_count()
    if cast == 1:
        print(tax_for_married_couple(income))
    elif cast == 2:
        print(tax_for_subject(income))


main()
