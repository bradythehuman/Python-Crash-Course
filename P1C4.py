# Comprehensions are a tool for creating lists compactly.
# The basic format is an output followed by a for loop.

var = [i for i in range(1, 10)]
print(var)

# However multiple for loops may be added, the output may be modified by functions or\
# operators and if statements may be attached after the for statements.

# 4-9 Cube Comprehension

cubes = [i ** 3 for i in range(1, 11) if (i ** 3) % 2 != 0]
print(cubes)

# Copying a list simply by setting one equal to another will not physically copy the\
# list, it will only make a secondary pointer to the origional list. As such any changes\
# to the original will effect the copy. Slicing the list into a single piece when\
# copying eliminates this issue.

list_a = [1, 2, 3]
list_b = list_a
list_c = list_a[:]
print(list_a, list_b, list_c)

list_a[0] = 3
list_c[1] = 3
print(list_a, list_b, list_c)

# An immutable list is a tuple. Rewriting the variable is acceptable but attempting to\
# alter individual elements raises an error.
