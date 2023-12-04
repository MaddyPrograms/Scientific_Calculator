import math

def add(x, y):
  """Adds two numbers and returns the sum."""
  return x + y

def subtract(x, y):
  """Subtracts the second number from the first and returns the difference."""
  return x - y

def multiply(x, y):
  """Multiplies two numbers and returns the product."""
  return x * y

def divide(x, y):
  """Divides the first number by the second and returns the quotient.
  Checks for division by zero and displays an error message."""
  if y == 0:
    print("Error: Division by zero is undefined. Please enter a non-zero divisor.")
    return None
  else:
    return x / y

def square_root(x):
  """Calculates the square root of a number and returns the result.
  Checks for negative input and displays an error message."""
  if x < 0:
    print("Error: Square root of a negative number is not real.")
    return None
  else:
    return math.sqrt(x)

def logarithm(x, base):
  """Calculates the logarithm of a number to a given base and returns the result.
  Checks for invalid input and displays an error message."""
  if x <= 0 or base <= 0 or base == 1:
    print("Error: Invalid input for logarithm. Please ensure x > 0 and base > 0 and base != 1.")
    return None
  else:
    return math.log(x, base)

def power(x, y):
  """Raises the first number to the power of the second and returns the result."""
  return math.pow(x, y)

def factorial(x):
  """Calculates the factorial of a number and returns the result.
  Checks for negative or non-integer input and displays an error message."""
  if x < 0:
    print("Error: Factorial of a negative number is not defined.")
    return None
  elif not isinstance(x, int):
    print("Error: Factorial is only defined for non-negative integers.")
    return None
  else:
    return math.factorial(x)

def sine(x):
  """Calculates the sine of an angle in radians and returns the result."""
  return math.sin(x)

def cosine(x):
  """Calculates the cosine of an angle in radians and returns the result."""
  return math.cos(x)

def tangent(x):
  """Calculates the tangent of an angle in radians and returns the result."""
  return math.tan(x)

def arcsin(x):
  """Calculates the arcsine of a value and returns the angle in radians.
  Checks for invalid input and displays an error message."""
  if abs(x) > 1:
    print("Error: Arcsine is only defined for values between -1 and 1.")
    return None
  else:
    return math.asin(x)

def arccos(x):
  """Calculates the arccosine of a value and returns the angle in radians.
  Checks for invalid input and displays an error message."""
  if abs(x) > 1:
    print("Error: Arccosine is only defined for values between -1 and 1.")
    return None
  else:
    return math.acos(x)

def arctan(x):
  """Calculates the arctangent of a value and returns the angle in radians."""
  return math.atan(x)

def round_to_decimal(x, n):
  """Rounds a number to the specified number of decimal places and returns the result."""
  return round(x, n)

def absolute_value(x):
  """Calculates the absolute value of a number and returns the result."""
  return abs(x)

def history():
  """Displays a list of past calculations (to be implemented)."""
  print("History feature not yet implemented.")

def custom_function():
  """Defines a custom function using existing operations (to be implemented)."""
  print("Custom function feature not yet implemented.")

def graph(function):
  """Plots the graph of a function (to be implemented)."""
  print("Graphing feature not yet implemented.")

def main():
  """Prints the menu and handles user input and function calls."""
  print("Welcome to the enhanced calculator!")
  print("Enter 'help' for a list of available functions.")

  while True:
    choice = input("Enter your choice:
