import math


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

def log(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Logarithm arguments must be positive and base cannot be 1")
    return math.log(b, a)

def exp(a, b):
    return a ** b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def logarithm(a, b):
    if a <= 1 or b <= 0:
        raise ValueError("Error: a must be greater that 1 and b must be greater than 0")
    return math.log(a, b)


def exponent(a, b):
    return a**b

