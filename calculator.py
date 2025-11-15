import math


def square_root(a):
    if a < 0:
        raise ValueError("A cannot be less than 0")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b


def exp(a, b):
    return a ** b


def subtract(a, b):
    return a - b


def logarithm(a, b):
    if a == 1 or a <= 0 or b <= 0:
        raise ValueError("Error: a must be greater that 1 and b must be greater than 0")
    return math.log(a, b)
