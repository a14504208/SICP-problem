from math import gcd

class Rational:
    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.value = (numer // g, denom // g)

    def numer(self):
        return self.value[0]

    def denom(self):
        return self.value[1]

    def __str__(self):
        return '{0} / {1}'.format(self.numer(), self.denom())

    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer(), self.denom())

    def __add__(self, rat):
        n1, d1 = self.numer(), self.denom()
        n2, d2 = rat.numer(), rat.denom()

        return Rational(n1 * d2 + n2 * d1,
                        d1 * d2)

    def __sub__(self, rat):
        n1, d1 = self.numer(), self.denom()
        n2, d2 = rat.numer(), rat.denom()

        return Rational(n1 * d2 - n2 * d1,
                        d1 * d2)

    def __mul__(self, rat):
        n1, d1 = self.numer(), self.denom()
        n2, d2 = rat.numer(), rat.denom()
        
        return Rational(n1 * n2,
                        d1 * d2)

    def __truediv__(self, rat):
        n1, d1 = self.numer(), self.denom()
        n2, d2 = rat.numer(), rat.denom()

        return Rational(n1 * d2,
                        d1 * n2)

    def __eq__(self, rat):
        return (self.numer() == rat.numer()) and (self.denom() == rat.denom())
        
