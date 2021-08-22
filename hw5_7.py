average_profit = 0
profit_firms = {}

with open('test_7.txt') as f:
    entries = f.read().split('\n')
    entries = filter(lambda el: bool(el), entries)

    for entry in entries:
        [name, mfo_code, expenses, proceeds] = entry.split(' ')

        firm_profit = int(expenses) - int(proceeds)
        profit_firms[name] = firm_profit

        if firm_profit > 0:
            average_profit = firm_profit if average_profit == 0 else (average_profit + firm_profit) / 2


result = [profit_firms, {average_profit: average_profit}]

print(result)
