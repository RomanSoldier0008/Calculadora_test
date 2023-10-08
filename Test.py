import unittest
from Addition import *
from Subtraction import Subtraction
from Multiplication import Multiplication
from Division import Division

class Test(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Addition(2, 2).add(), RETURN_TOTAL.format(4), print(MESSAGE_TEST))

    def test_subtraction(self):
        self.assertEqual(Subtraction(10, 5).subtract(), RETURN_TOTAL.format(5), MESSAGE_TEST)

    def test_multiplication(self):
        self.assertEqual(Multiplication(4, 4).multiply(), RETURN_TOTAL.format(16), MESSAGE_TEST)

    def test_division(self):
        self.assertEqual(Division(5, 5).split(), RETURN_TOTAL.format(1), MESSAGE_TEST)