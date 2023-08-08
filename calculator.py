import math
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y !=0:
        return x/y
    else:
        return "Can't divide by zero"

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Invalid Input"
    
def logarithm (x, base):
    if x > 0 and base > 0 and base != 1:
        return math.log(x, base)
    else:
        return "Invalid Input"
    
while True:
    print("Options:")
    print("Enter '1' for addition")
    print("Enter '2' for subtraction")
    print("Enter '3' for multiplication")
    print("Enter '4' for division")
    print("Enter '5' for square root")
    print("Enter '6' for logarithm")
    print("Enter '7' to quit")

    choice = input("Enter your choice: ")

    if choice == '7':
        break

    if choice in ('1', '2', '3', '4', '5', '6'):
        if choice in ('1', '2', '3', '4', '6'):
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        else:
            x = float(input("Enter the number: "))
