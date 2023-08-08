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