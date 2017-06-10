# The following code is a mess around with classes.

import P1C9_class_mod

tomahawk = P1C9_class_mod.Missile('300 meters', 'cold war',
                                  'long and pointy', 'nuclear', dud=True)
tomahawk.explode()
tomahawk.dud = False
tomahawk.launch('Russia')

# The super(). function refers to the following function in the parent class even if the\
# function was renamed in the child class.

# If a class is getting crowded some aspects can be broken into a parallel class whose\
# initialization is part of the primary classes initialization.

# When importing classes, only the initialization requires a namespace as that namespace\
# is then incorporated into the instance that is used to call subsequent functions and or\
# variables.

# When importing multiple classes or functions from a module, they can be listed and\
# separated with commas. Modules imported into other modules will be imported with the\
# primary module.

# There is a class called OrderedDict in the collections module which is part of the\
# standard library. It has the same methods as a regular dictionary as it is a basically\
# unaltered subclass. The only difference is that it keeps track of the order in which\
# key value pairs are added. Therefore when using a for loop the items will come back\
# in the order given.
