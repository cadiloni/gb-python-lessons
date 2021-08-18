"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не
должен быть бесконечным. Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
завершаем цикл. Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет
прекращено.
"""
from itertools import count
from itertools import cycle


def counter_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)


def cycle_func(my_list, iteration):
    i = 0
    iterator = cycle(my_list)
    while i < iteration:
        print(next(iterator))
        i += 1


counter_func(start_number=int(input("Start number: ")), stop_number=int(input("Stop number: ")))
cycle_func(my_list=[7, 5, 7], iteration=int(input("Enter number of times iteration will run: ")))
