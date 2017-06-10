# Arguments can be passed to functions as arguments and/or keyword arguments. Default\
# arguments must be written after required ones.

# Because empty variables evaluate to false defaulting a optional variable to nothing\
# and then using an if statement is an effective way to ensure its optionality.


def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician, '\n')

# Any amount of arguments can be passed into a function by using *args or *kwargs. In\
# order to mix positional and arbitrary arguments the arbitrary ones must be placed\
# after the positional ones. The default arguments still are positioned last.


def make_pizza(size, *toppings, crust='plain', sauce='red', **other):
    print(f'One {size} pizza with ' + ', '.join(toppings) +
          f', {sauce} sauce and {crust} crust, coming right up.')
    temp = [other[key] + ' ' + key for key in other]
    print('I also have ' + ', '.join(temp[1:]) + ' and ' + temp[0] + ' for ya.\n')

make_pizza('large', 'peperoni', 'sausage', 'olives',
           sauce='pesto', soda='orange', bread='cheesy', pepper='diet dr.')

# Modules can be imported in 3 ways. The entire module, a single function or the entire\
# module as if it was part of the same program.
# Pointers can be made to point to functions similar to data structures. This can be\
# done during import using the as statement or later by assigning a variable to a function\
# without its parenthesis.

import csv as c
from csv import writer as w

r = c.reader


def csv_snip(path, output_path):
    """
    Create a copy of csv file that contains only the first 2 columns.
    :param path: The path of the original csv file.
    :param output_path: The path of the new csv file.
    :return: 
    """
    with open(path, 'r') as f_obj:
        reader = r(f_obj)
        output = []
        for row in reader:
            output.append(row[:2])

        with open(output_path, 'w', newline='') as f_obj_w:
            writer = w(f_obj_w, delimiter=',')
            for line in output:
                writer.writerow(line)

csv_snip('P1C8_data1.csv', 'P1C8_data2.csv')

# An asterisk will import all functions from a module and remove the need for any namespace.

# from module_name import *
