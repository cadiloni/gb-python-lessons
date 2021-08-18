"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает
за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

from math import factorial
from itertools import count


def fact():
    for el in count(1):
        yield factorial(el)


n = int(input("Enter the NUMBER to find factorial "))
gen = fact()
x = 0

for i in gen:
    if x < n:
        print(i)
        x += 1
    else:
        break
