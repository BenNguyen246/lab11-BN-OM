import math


def square_root(a):
    if a < 0:
        raise ValueError("A cannot be less than 0")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Error: a cannot be 0")
    return b / a


def logarithm(a, b):
    if a <= 1 or b <= 0:
        raise ValueError("Error: a must be greater that 1 and b must be greater than 0")
    return math.log(a, b)


def exponent(a, b):
    return a ** b
