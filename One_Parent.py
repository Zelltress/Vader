taxes_percent = [0, .1, .15, .25, .28, .33, .35, .396]

def one_parent(taxable_money):
    brackets_for_parent = [0, 12950, 49400, 127550, 206600, 405100, 432200]
    parent_tax = 0
    remains = taxable_money
    for i in range(len(brackets_for_parent)-1):
        if taxable_money > brackets_for_parent[i+1]:
            parent_tax += taxes_percent[i+1]*(brackets_for_parent[i+1]-brackets_for_parent[i])
            remains -= brackets_for_parent[i+1]-brackets_for_parent[i]
        else:
            parent_tax += remains*taxes_percent[i+1]
            break
    return parent_tax

print(one_parent(37924))
