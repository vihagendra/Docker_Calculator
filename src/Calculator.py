def addition(a, b):
    return a + b


def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c


def multiplication(a, b):
    return a * b


def division(a, b):
    a = float(a)
    b = float(b)
    return round(b / a, 9)


def squaring(a):
    return int(a) ** 2


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def sqr(self, a):
        self.result = squaring(a)
        return self.result

