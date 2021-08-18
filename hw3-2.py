"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def my_func(name, surname, byear, city, email, phone):
    print(name, surname, byear, city, email, phone)


my_func(name='Steven', surname='Howking', byear=1959, city='San Jose', email='mail', phone='23423423344')


"""
# Not completed yet

fields = ('name', 'age', 'year', 'city', 'email', 'telephone')
data = []

def user_data(fields):
    while True:
        change = input("Press any button to continue or 'q' to quit the program")
        if change == 'q':
            break
        person = {}
        for field in fields:
            person[field] = input(f'Enter the value of the field - {field} ')
        data.append(person)
    return ' '.join(fields)
"""
