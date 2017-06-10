# Because empty lists evaluate to false the following code can be used to sort a list\
# into two separate lists.

list_original = [i ** 2 for i in range(1, 11)]
list_odd = []
list_even = []
print(list_original)

while list_original:
    num = list_original.pop()
    if num % 2 == 0:
        list_even.append(num)
    else:
        list_odd.append(num)

list_odd.sort()
list_even.sort()
print(list_odd, list_even, '\n')

# The following function aims to remove all names from a list that start with the letter\
# b using a while loop with an in statement.

names = ['tom', 'brady', 'burt', 'harold', 'bethany', 'julia', 'ron']
print(names)

n = []
for i in range(len(names)):
    n.append(names[i][0].lower())
while 'b' in n:
    i = n.index('b')
    del n[i]
    del names[i]
print(names, '\n')

# If the in statement missed out, the above code may be simplified to...

names = ['tom', 'brady', 'burt', 'harold', 'bethany', 'julia', 'ron']
print(names)

i = 0
while i < len(names):
    if names[i][0].lower() == 'b':
        names.remove(names[i])
    else:
        i += 1
print(names, '\n')
