import statistics

with open('test_3.txt') as f:
    lines = filter(lambda e: bool(e), f.read().split('\n'))
    parts = (el.split(':') for el in lines)
    salaries = []

    for entry in parts:
        name = entry[0]
        salary = int(entry[1])
        salaries.append(salary)

        if salary < 20000:
            print(f'Employee {name} has salary less the 20K (Salary: {salary})')


print(f'Average salary: {statistics.mean(salaries)}')