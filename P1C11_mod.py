def format_name(first, last, middle=''):
    if middle:
        full = f'{first} {middle} {last}'
    else:
        full = f'{first} {last}'
    return full.title()


def location(city, country, pop=''):
    if pop:
        description = city + ', ' + country + ' - population ' + str(pop)
    else:
        description = city + ', ' + country
    return description.title()


class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, increase=5000):
        self.salary += increase
