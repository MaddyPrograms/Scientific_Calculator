import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x/y
    else:
        return "Can't divide by zero"

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Invalid Input"
    
def logarithm(x, base):
    if x > 0 and base > 0 and base != 1:
        return math.log(x, base)
    else:
        return "Invalid Input"

def power(x, y):
    return math.pow(x, y)

def factorial(x):
    if x < 0:
        return "Invalid Input"
    elif x == 0 or x == 1:
        return 1
    else:
        return math.factorial(x)

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)

def arcsin(x):
    return math.asin(x)

def arccos(x):
    return math.acos(x)

def arctan(x):
    return math.atan(x)

def round_to_decimal(x, n):
    return round(x, n)

def absolute_value(x):
    return abs(x)

while True:
    print("Options:")
    print("Enter '1' for addition")
    print("Enter '2' for subtraction")
    print("Enter '3' for multiplication")
    print("Enter '4' for division")
    print("Enter '5' for square root")
    print("Enter '6' for logarithm")
    print("Enter '7' for power")
    print("Enter '8' for factorial")
    print("Enter '9' for sine")
    print("Enter '10' for cosine")
    print("Enter '11' for tangent")
    print("Enter '12' for arcsin")
    print("Enter '13' for arccos")
    print("Enter '14' for arctan")
    print("Enter '15' for rounding")
    print("Enter '16' for absolute value")
    print("Enter '17' to quit")

    choice = input("Enter your choice: ")

    if choice == '17':
        break

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'):
        if choice in ('1', '2', '3', '4', '6', '7'):
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        elif choice in ('9', '10', '11', '12', '13', '14'):
            x = float(input("Enter the angle in radians: "))
        else:
            x = float(input("Enter the number: "))

        if choice == '1':
            print("Result:", add(x, y))
        elif choice == '2':
            print("Result:", subtract(x, y))
        elif choice == '3':
            print("Result:", multiply(x, y))
        elif choice == '4':
            print("Result:", divide(x, y))
        elif choice == '5':
            print("Result:", square_root(x))
        elif choice == '6':
            base = float(input("Enter the base for logarithm: "))
            print("Result:", logarithm(x, base))
        elif choice == '7':
            print("Result:", power(x, y))
        elif choice == '8':
            print("Result:", factorial(x))
        elif choice == '9':
            print("Result:", sine(x))
        elif choice == '10':
            print("Result:", cosine(x))
        elif choice == '11':
            print("Result:", tangent(x))
        elif choice == '12':
            print("Result:", arcsin(x))
        elif choice == '13':
            print("Result:", arccos(x))
        elif choice == '14':
            print("Result:", arctan(x))
        elif choice == '15':
            n = int(input("Enter the number of decimal places: "))
            print("Result:", round_to_decimal(x, n))
        elif choice == '16':
            print("Result:", absolute_value(x))
    else:
        print("Invalid input")
