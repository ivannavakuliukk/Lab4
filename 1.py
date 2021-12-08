from math import gcd


class Rational:
    def __init__(self, numerator = 1, denominator = 2):
        self.numerator = numerator
        self.denominator = denominator
        red = self.reduce()
        self.numerator = red.numerator
        self.denominator = red.denominator

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    @numerator.setter
    def numerator(self, numerator):
        if not isinstance(numerator, int):
            raise TypeError
        self._numerator = numerator

    @denominator.setter
    def denominator(self, denominator):
        if not isinstance(denominator, int):
            raise TypeError
        if not denominator:
            raise ValueError("division by zero")
        self._denominator = denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def floating(self):
        return self.numerator/self.denominator

    def reduce(self):
        divisor = gcd(self.numerator, self.denominator)
        if divisor == 1:
            return self
        return Rational(int(self.numerator // divisor), int(self.denominator // divisor))

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Rational(numerator, denominator)

    def __lt__(self, other):
        return Rational(self.numerator, self.denominator) < Rational(other.numerator, other.denominator)


num1 = Rational(1, 2)
num2 = Rational(1, 4)
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
