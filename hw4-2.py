"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента
"""
given_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
outcome = [el for el in given_list if el > given_list[given_list.index(el) - 1]]
print(outcome)
