import math


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
