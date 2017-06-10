import unittest

from P1C11_mod import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.sales = Employee('John', 'Wick', 110000)

    def test_raise(self):
        self.sales.give_raise()
        self.assertEqual(self.sales.salary, 115000)

    def test_custom_raise(self):
        self.sales.give_raise(2000)
        self.assertEqual(self.sales.salary, 112000)

if __name__ == '__main__':
    unittest.main()
