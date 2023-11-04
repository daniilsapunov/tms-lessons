class Rational:
    def __init__(self, __numerator, __denominator):
        self.__numerator = __numerator
        self.__denominator = __denominator
        self.__normalise()

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        return f'{self.numerator} / {self.denominator}'

    def __mul__(self, other: 'Rational') -> 'Rational':
        return Rational((self.numerator * other.__numerator), (self.denominator * other.denominator))

    def __truediv__(self, other: 'Rational') -> 'Rational':
        return Rational((self.numerator * other.denominator), (self.denominator * other.numerator))

    def __add__(self, other: 'Rational') -> 'Rational':
        return Rational((self.numerator * other.denominator + self.denominator * other.numerator),
                        (self.denominator * other.denominator))

    def __sub__(self, other: 'Rational') -> 'Rational':
        return Rational((self.numerator * other.denominator - self.denominator * other.numerator),
                        (self.denominator * other.denominator))

    def __eq__(self, other: 'Rational'):
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __ne__(self, other: 'Rational'):
        return self.numerator * other.denominator != self.denominator * other.numerator

    def __lt__(self, other: 'Rational'):
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __gt__(self, other: 'Rational'):
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __le__(self, other: 'Rational'):
        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __ge__(self, other: 'Rational'):
        return self.numerator * other.denominator >= self.denominator * other.numerator

    def __normalise(self):

        """NOD = math.gcd(self.numerator, self.denominator)"""
        gcd = 1
        if self.numerator > self.denominator:
            t = self.denominator
        else:
            t = self.numerator
        for i in range(1, t + 1):
            if (self.numerator % i == 0) and (self.denominator % i == 0):
                gcd = i
        self.__numerator //= gcd
        self.__denominator //= gcd

        if self.denominator < 0:
            self.__numerator *= -1
            self.__denominator *= -1


if __name__ == '__main__':
    first_number = Rational(1, 2)
    second_number = Rational(3, 2)

    assert first_number * second_number == Rational(3, 4)
    assert first_number / second_number == Rational(2, 6)
    assert first_number + second_number == Rational(4, 2)
    assert first_number - second_number == Rational(-2, 2)
    assert first_number * second_number != Rational(2, 4)
    assert first_number * second_number >= Rational(1, 7)
    assert first_number * second_number <= Rational(4, 1)
    assert first_number * second_number < Rational(6, 1)
    assert first_number * second_number > Rational(1, 2)
    assert Rational(-1,-2) == Rational(1,2)
    assert Rational(5,-2) == Rational(-5,2)
    f = Rational(1,4)
    s = Rational(3,2)
    t = Rational(1,8)
    ff = Rational(156,100)
    assert f * (s + t) + ff == Rational(1573,800)

