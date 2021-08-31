result = {}

with open('test_6.txt') as f:
    lines = f.read().split('\n')
    lines = filter(lambda el: bool(el), lines)

    parts = (el.split(':') for el in lines)

    for entry in parts:
        lesson_name = entry[0].strip()
        lessons = entry[1].split(' ')
        lessons = filter(lambda el: bool(el), lessons)

        total_lessons = 0

        for lesson in lessons:
            part = lesson.strip('lec|pr|lab')

            if not part.isdigit():
                raise ValueError(f'Invalid format in {lesson}')

            total_lessons += int(part)

        result[lesson_name] = total_lessons


print(result)
