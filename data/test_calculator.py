import unittest
from simple_calculator import Calculator, fun


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

    def test_divide(self):
        calc_value = self.calculator.value
        self.assertEquals(self.calculator.divide(2, 3).value, calc_value / 6)

    def test_file_read(self):
        with open('file.txt', 'r') as f:
            text = f.read()
            self.assertEquals(fun(text), text[::-1])

    def kek(self):
        self.assertEqual(1, 2)


if __name__ == '__main__':
    unittest.main()


