from constants import *
class Division:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.total = 0

    def split(self):
        self.total = (self.num1 // self.num2)
        return RETURN_TOTAL.format(self.total)