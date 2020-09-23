import unittest
from simple_calculator import Calculator, fun
from math import sqrt
from random import random


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(1)

    def test_add(self):
        """
        Test add function with regular data
        :rtype: object
        """
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.add(1, 2, 3).value, calc_value + 6)

    def test_mul(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.multiply(5, 2, 90).value, calc_value * 900)

    def test_mul_zero(self):
        self.calculator.value = 4
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.multiply(5, 2, 90, 0).value, 0)

    def test_divide(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.divide(2, 3).value, calc_value / 6)

    def test_divide_int(self):
        self.calculator.value = 20
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.divide(2, 4, integer_divide=True).value, calc_value // 8)

    def test_subtract(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.subtract(1, 2).value, calc_value - (1 + 2))

    def test_subtract_negative(self):
        self.calculator.value = 10
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.subtract(-11, -2).value, calc_value + 11 + 2)

    def test_power(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(1, 2).value, calc_value**2)

    def test_zero_power(self):
        self.calculator = 10
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(1, 0, 2).value, 1)

    def test_negative_power(self):
        self.calculator.value = 10
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(-1, -2).value, calc_value**2)

    def test_root(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.root().value, sqrt(calc_value))

    def test_zero_root(self):
        self.calculator.value = 0
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.root().value, 0)

    # def test_file_read(self):
    #     with open('file.txt', 'r') as f:
    #         text = f.read()
    #         self.assertEqual(fun(text), text[::-1])

    def kek(self):
        self.assertEqual(1, 2)


if __name__ == '__main__':
    unittest.main()
