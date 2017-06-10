# Simple data structures may be stored using JSON. The .dump() function takes two arguments, the data to store and a lo\
# cation to store it.

import json

data = (2, 5, 8, 11)
file_location = 'P1C10_folder\data.json'

with open(file_location,'w') as f_obj:
    json.dump(data, f_obj)
data = ()
print(f'data: {data}')

with open(file_location) as f_obj:
    data = json.load(f_obj)
print(f'data: {data}\n')

# The set (immutable) was stored as a list.

# 10-11 Favorite Number / 12 Favorite Number Remembered

number_file = r'P1C10_folder\number.json'


def test_file(path):
    try:
        number = find_number(path)
    except FileNotFoundError:
        ask_number(path)
        print('I won\'t forget it.')
    else:
        print(f'I know that your favorite number is {number}!')


def find_number(path):
    with open(path) as f_obj:
        number = json.load(f_obj)
    return number


def ask_number(path):
    with open(path, 'w') as f_obj:
        number = input('Enter your favorite number: ')
        json.dump(number, f_obj)

test_file(number_file)
