from constants import *
class Multiplication:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.total = 0

    def multiply(self):
        self.total = (self.num1 * self.num2)
        return RETURN_TOTAL.format(self.total)