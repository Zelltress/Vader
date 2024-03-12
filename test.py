import ru_local as ru
nomber = int(input(ru.CHOICE))
category = {1: 'Subject', 2: 'Married_couple', 3: 'Parent'}
print(category.get(nomber))
a = category.get(nomber)

