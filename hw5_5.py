def adding_nums_in_a_file():
    try:
        with open('test_5.txt', 'w+') as file_obj:
            line = input('Input the number with spaces \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Error in a file')
    except ValueError:
        print('Entered number is incorrect')


adding_nums_in_a_file()
