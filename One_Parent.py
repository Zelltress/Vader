MAX_MONTH = 12
name_month = ['', 'январе', 'феврале', 'марте', 'апреле', 'мае', 'июне',
        'июле', 'августе', 'сентябре', 'октябре', 'ноябре', 'декабре']

# Функция income_count() возвращает сумму доходов за год
def income_count():
    sum_of_income = 0
    for month in range(1, MAX_MONTH + 1):
        value_in_month = float(input(f' {'Доход в '} {name_month[month]} [USD]: ')) #изменить на значение рулокал 'ru.TEXT_INCOME'
        sum_of_income += value_in_month
    return sum_of_income

def tax_free_count():
    amount = 0
    for month in range(1, MAX_MONTH + 1):
        free_amnt_mnth = float(input(f' {'Сумма не облагаемая налогом в '} {name_month[month]} [USD]: ')) #ru.FREE_TAX и INCOME
        amount += free_amnt_mnth
    return amount

taxes_percent = [0, .1, .15, .25, .28, .33, .35, .396]

cast = input()
def one_parent(taxable_money):
    brackets_for_parent = [0, 12950, 49400, 127550, 206600, 405100, 432200]
    parent_tax = 0
    remains = taxable_money
    for i in range(len(brackets_for_parent)):
        if taxable_money > brackets_for_parent[i]:
            parent_tax += taxes_percent[i]*(brackets_for_parent[i+1]-brackets_for_parent[i])
            remains -= brackets_for_parent[i+1]-brackets_for_parent[i]
        else:
            parent_tax += remains*taxes_percent[i]
        break
    print(parent_tax) #gtf
    return parent_tax

if cast == 3:
    print(one_parent(37924))
