"""
* Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (
характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя.
"""

products, order = [], 1
title, price, amount = None, None, None

while True:
    if title is None:
        tmp = input('Name of the Product ')
        if not tmp.isalnum():
            print('Title of the product can not be empty. Please try one more time.')
            continue

        title = tmp

    if price is None:
        tmp = input('Price of the Product: ')
        if not tmp.isdigit():
            print('Price must be in numbers. Try one more time.')
            continue

        price = int(tmp)

    if amount is None:
        tmp = input('Amount of product: ')
        if not tmp.isdigit():
            print('Quantity must be in numbers. Try one more time.')
            continue

        amount = int(tmp)

    tmp = input('Write the units : ')
    if not tmp.isalpha():
        print('Unit of item can not be empty. Try again.')
        continue

    unit = tmp

    products.append((
        order,
        {
            'title': title,
            'price': price,
            'amount': amount,
            'unit': unit
        }
    ))

    title, price, amount = None, None, None
    order += 1

    print(products)

    exit_program = input('Do you want to exit: Type (Y/N)')
    if exit_program.lower() == 'y':
        break

analytics = {
    'title': [],
    'price': [],
    'amount': [],
    'unit': set()
}

for _, item in products:
    analytics['title'].append(item['title'])
    analytics['price'].append(item['price'])
    analytics['amount'].append(item['amount'])
    analytics['unit'].add(item['unit'])

print(analytics)
