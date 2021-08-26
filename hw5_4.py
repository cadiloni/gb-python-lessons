words_to_change = {
    'One': 'Odin',
    'Two': 'Dva',
    'Three': 'Tri',
    'Four': 'Chetire'
}

with open('test_4.txt', 'r') as input_file:
    with open('test_4_output.txt', 'w') as output_file:
        for line in input_file:
            parts = line.split('-')
            parts = list(map(lambda el: str(el).strip(), parts))

            for key in words_to_change.keys():
                parts[0] = str(parts[0]).replace(key, words_to_change[key])

            output_file.write(f'{parts[0]} - {parts[1]}\n')
