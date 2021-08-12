"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

"""
my_list = [7, 5, 3, 3, 2]
print(my_list)
while True:
    item = input('Please enter the number and the program will append it in to the list correct way ')
    if not item.isdigit():
        print('Please enter any number again')
        continue
    else:
        item = int(item)

    idx = None

    for i, num in enumerate(my_list):
        if item > num:
            idx = i
            break

    if idx is None:
        my_list.append(item)
    else:
        my_list.insert(idx, item)

    print(my_list)

    exit_program = input('Do you want to exit: Type (Y/N)')
    if exit_program.lower() == 'y':
        break
