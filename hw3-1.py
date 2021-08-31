"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль """


def division(*args):
    try:
        arg1 = int(input("Dividend is - "))
        arg2 = int(input("Divisor is - "))
        quotient = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Numbers can not be divided into zero"

    print(float(quotient))


division()
