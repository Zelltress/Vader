import ru_local as ru

nomber = int(input(ru.CHOICE))

MAX_MONTH = 12
category = {1: 'Subject', 2: 'Married_couple', 3: 'Parent'}
choice_ctgr = category.get(nomber)
taxes_percent = [0, .1, .15, .25, .28, .33, .35, .396]
brackets_for_couple = [0, 18150, 73800, 148850, 226850, 405100, 457600]
brackets_for_subject = [0, 9075, 36900, 89350, 186350, 405100, 406750]


def income_count():
    """
    The function that calculates the amount of annual income
    """
    sum_of_income = 0
    for month in range(1, MAX_MONTH + 1):
        value_in_month = float(input(f' {ru.TEXT_INCOME} {ru.PERIOD[month]} [USD]: '))
        sum_of_income += value_in_month
    return sum_of_income


def tax_free_count():
    """
    The function that calculates the annual tax-free amount
    """
    amount = 0
    for month in range(1, MAX_MONTH + 1):
        free_amnt_mnth = float(input(f' {ru.FREE_TAX} {ru.PERIOD[month]} [USD]: '))
        amount += free_amnt_mnth
    return amount


def tax_for_married_couple(taxable_money):
    """
    The function that calculates the annual tax for married couple
    """
    couple_tax = 0
    left_money = taxable_money
    for i in range(1, len(brackets_for_couple)):
        if taxable_money > brackets_for_couple[i]:
            couple_tax += (brackets_for_couple[i] - brackets_for_couple[i - 1]) * taxes_percent[i]
            left_money -= brackets_for_couple[i] - brackets_for_couple[i - 1]
        else:
            couple_tax += left_money * taxes_percent[i]
            break
    if taxable_money > brackets_for_couple[6]:
        couple_tax += taxes_percent[7] * (taxable_money - brackets_for_couple[6])
    return couple_tax


def tax_for_subject(taxable_money):
    """
    The function that calculates the annual tax for subject
    """
    subject_tax = 0
    leftover = taxable_money
    for i in range(1, len(brackets_for_subject)):
        if taxable_money > brackets_for_subject[i]:
            subject_tax += (brackets_for_subject[i] - brackets_for_subject[i - 1]) * taxes_percent[i]
            leftover -= brackets_for_subject[i] - brackets_for_subject[i - 1]
        else:
            subject_tax += leftover * taxes_percent[i]
            break
    if taxable_money > brackets_for_subject[6]:
        subject_tax += taxes_percent[7] * (taxable_money - brackets_for_subject[6])
    return subject_tax


def tax_for_parent(taxable_money):
    """
    The function that calculates the annual tax for one parent
    """
    brackets_for_parent = [0, 12950, 49400, 127550, 206600, 405100, 432200]
    parent_tax = 0
    remains = taxable_money
    for i in range(len(brackets_for_parent) - 1):
        if taxable_money > brackets_for_parent[i + 1]:
            parent_tax += taxes_percent[i + 1] * (brackets_for_parent[i + 1] - brackets_for_parent[i])
            remains -= brackets_for_parent[i + 1] - brackets_for_parent[i]
        else:
            parent_tax += remains * taxes_percent[i + 1]
            break
    if taxable_money > brackets_for_parent[6]:
        parent_tax += taxes_percent[7] * (taxable_money - brackets_for_parent[6])
    return parent_tax


def main():
    income = income_count() - tax_free_count()
    if choice_ctgr == 'Married_couple':
        print(tax_for_married_couple(income))
    elif choice_ctgr == 'Subject':
        print(tax_for_subject(income))
    else:
        print(tax_for_parent(income))


if __name__ == '__main__':
    main()
