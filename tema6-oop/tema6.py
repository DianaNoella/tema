import math


class Fraction:
    def __init__(self, numerator, denominator):
        try:
            numerator = int(numerator)
        except ValueError:
            raise ValueError('Numerator must be an integer')

        try:
            denominator = int(denominator)
        except ValueError:
            raise ValueError('Denominator must be an integer')

        if denominator == 0:
            raise ValueError('Fraction cannot have denominator equal to 0')

        self._numerator, self._denominator = self._get_simplified(numerator, denominator)

    @staticmethod
    def _get_simplified(numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        return numerator // gcd, denominator // gcd

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    def __add__(self, other):
        lcm = math.lcm(self._denominator, other.denominator)
        first_fraction_numerator = self._numerator * (lcm // self._denominator)
        second_fraction_numerator = other.numerator * (lcm // other.denominator)

        return Fraction(first_fraction_numerator + second_fraction_numerator, lcm)


    def __sub__(self, other):
        lcm = math.lcm(self._denominator, other.denominator)
        first_fraction_numerator = self._numerator * (lcm // self._denominator)
        second_fraction_numerator = other.numerator * (lcm // other.denominator)

        return Fraction(first_fraction_numerator - second_fraction_numerator, lcm)

    def inverse(self):
        return Fraction(self._denominator, self._numerator)

    def __str__(self):
        return f'{self._numerator}/{self._denominator}'

if __name__ == '__main__':
    pass

    # x = Fraction(1, 5)
    # print('x', x)
    #
    # y = Fraction(2, 5)
    # print('y', y)
    #
    # z = x + y
    # print('z', z)
