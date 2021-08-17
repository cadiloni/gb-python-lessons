"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input().
"""

element_amount = int(input("Write the amount of elements which the list should contain "))
my_list = []
i = 0
element = 0

while i < element_amount:
    my_list.append(input("Fill in your list "))
    i += 1

for items in range(int(len(my_list) / 2)):
    my_list[element], my_list[element + 1] = my_list[element + 1], my_list[element]
    element += 2
print(my_list)
