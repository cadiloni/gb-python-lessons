file = open('test_2.txt', 'r')

file_data = file.read()

count_lines = len(list(filter(lambda e: bool(e), file_data.split('\n'))))
count_words = len(list(filter(lambda e: bool(e), file_data.replace('\n', ' ').split(' '))))

print(f'Count lines in file: {count_lines} \nCount words in file: {count_words}')
