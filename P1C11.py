# Unit test example given.

import unittest

from P1C11_mod import format_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = format_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle(self):
        formatted_name = format_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()

# 11-1,2

from P1C11_mod import location


class TestLocation(unittest.TestCase):
    def test_city_country(self):
        description = location('boston', 'america')
        self.assertEqual(description, 'Boston, America')

    def test_city_country_pop(self):
        description = location('seattle', 'america', 1700000)
        self.assertEqual(description, 'Seattle, America - Population 1700000')

if __name__ == '__main__':
    unittest.main()
