# Below are possible ways to open a text file. The open functions second parameter\
# defaults to read only mode ('r) but can be made to read and write with 'r+', clear\
# and then write with 'w' or append with 'a'. The read() function will turn the file\
# into a single string containing newline characters (\n).

path = r'P1C10_folder\pi.txt'

with open(path) as f_obj:  # Method 1
    for line in f_obj:
        print(line.rstrip())
    long_str = f_obj.read()
    print(long_str.rstrip())

print()

f_obj = open(path)  # Method 2
print(f_obj)
print(f_obj.readlines())
f_obj.close()

# Both of the above methods work but with method 1 there is no need to worry over whether\
# the file was closed.

# Method 2 also uses .readlines() method which turns each line into a string within a list\
# that represents the entire file.

# .rstrip() is a string method which removes whitespace from the right side of the string.\
# This method is used because .read() always reads a newline character when it reaches\
# the end of a file.

# The first method only prints the file once because by the time the .read() is reached the\
# f_obj is empty.

path_python = r'P1C10_folder\in_python.txt'

# In python you can create classes with methods and properties.
# In python you can call prebuilt classes like str and int to hold normal data.
# In python you can treat variables simply as pointers to other objects.
# In python you can think of everything as an object.

print()

with open(path_python, 'r+') as f_obj:
    reader = f_obj.readlines()
    for line in reader:
        print(line.rstrip())
    print()

    if 'python' in reader[0]:
        find_str = 'python'
        replace_str = 'C'
    else:
        find_str = 'C'
        replace_str = 'python'

    output = []
    for line in reader:
        line = line.replace(find_str, replace_str)
        print(line.rstrip())
        output.append(line)
    f_obj.truncate(0)
    f_obj.writelines(output)

# Try except statements can be useful to avoid crashes if the program fails or to keep\
# end users from seeing the unnecessary details of the error. This can be to keep from\
# confusing the user or to keep malicious users from discovering exploits.

print()

x = 1
try:
    1 / x
except ZeroDivisionError:
    print('this is printed only in the event of the listed error occurring (try except statement 1).')
else:
    print('this is printed only if there is no error (try except statement 1).')

x = 0
try:
    1 / x
except ZeroDivisionError:
    print('this is printed only in the event of the listed error occurring (try except statement 2).')
else:
    print('this is printed only if there is no error (try except statement 2).')

# The else statement on a try except statement will only run if the

try:
    with open(path_python) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print(f'File with path {path_python} not found.')
else:
    words = contents.split()
    print()
    print(str(len(words)) + ' words')
    print(str(contents.lower().count('in')) + " occurrences of the word 'in'.\n")

# The main place you should be worried about errors is from external sources. Tasks that depend on user input of a\
# certain amount of signal strength.

# 10-6

print('\nEnter q at any time to quit')

while True:
    a = input('Enter a number: ')
    if a == 'q':
        break
    b = input('Enter its divisor: ')
    if b == 'q':
        break

    try:
        c = int(a) / float(b)
    except ValueError:
        print('Please enter two numbers.')
    except ZeroDivisionError:
        print('No number may be divided by zero')
    else:
        print(f'{a} / {b} = {c}')