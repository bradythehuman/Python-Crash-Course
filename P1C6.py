# Dictionary key value pairs can be removed with the del statement.
# The value and key methods can be used to access only one element of the dictionary\
# in a manner similar to a list. The two methods take no arguments.

dict_a = {'one': 1, 'two': 2, 'three': 2, 'four': 4, 'one': 5}
print(dict_a['one'])
print(set(dict_a))

# This next example will map the ancestors of an individual.

brady = {'kristi': {'karen': {'grandpa selmer': 'unknown'},
                    'wain': 'unknown'},
         'steve': {'audrey': 'unknown',
                   'gary': 'unknown'}
         }
print(brady['kristi']['karen']['grandpa selmer'])
