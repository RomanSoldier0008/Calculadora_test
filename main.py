from Addition import *
from Subtraction import Subtraction
from Multiplication import Multiplication
from Division import Division
from Test import Test

def add_numbers():
    global num1, num2
    num1 = int(input(ADD_NUM))
    num2 = int(input(ADD_NUM))

while True:
    opc = int(input(MENU_OPC_INPUT))
    if 0 < opc < 5:
        add_numbers()

    if opc == 1:
        object_addition = Addition(num1, num2)
        print(object_addition.add())

    elif opc == 2:
        object_subtraction = Subtraction(num1, num2)
        print(object_subtraction.subtract())

    elif opc == 3:
        object_multiplication = Multiplication(num1, num2)
        print(object_multiplication.multiply())

    elif opc == 4:
        object_division = Division(num1, num2)
        print(object_division.split())

    elif opc == 5:
        object_test = Test()
        object_test.test_addition()
        object_test.test_subtraction()
        object_test.test_multiplication()
        object_test.test_division()

    elif opc == 6:
        print(EXIT)
        break

    else:
        print(ERROR_IN_OPTION)
        continue