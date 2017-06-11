class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def numer(self):
        return self.numer

    def denom(self):
        return self.denom

    def __add__(self, rat):
        n1, d1 = self.numer(), self.denom()
        n2, d2 = rat.numer(). rat.numer()

        return Rational(n1 * d2 + n2 * d1,
                        d1 * d2)

    def __sub__(self, rat):
        n1, d1 = self.numer(), self.denom()
        n2, d2 = rat.numer(). rat.numer()

        return Rational(n1 * d2 - n2 * d1,
                        d1 * d2)

    def __mul__(self, rat):
        n1, d1 = self.numer(), self.denom()
        n2, d2 = rat.numer(). rat.numer()
        
        return Rational(n1 * n2,
                        d1 * d2)

    def __truediv__(self, rat):
        n1, d1 = self.numer(), self.denom()
        n2, d2 = rat.numer(). rat.numer()

        return Rational(n1 * d2,
                        d1 * n2)

    def __eq__(self, rat):
        return (self.numer() == rat.numer()) and (self.denom() == rat.denom())
        
