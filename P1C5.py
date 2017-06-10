# An in statement can be used to produce a Boolean result for a check of\
# whether a list contains a certain item. The Boolean operator not could\
# be used to turn the below code false

list_a = ['tree', 'fern', 'moss']
if 'moss' in list_a:
    print('Moss has been found in list A.')

# Empty objects such as lists will evaluate to false.

list_b = []
if not list_b:
    print('List B is empty.')