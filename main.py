class Fraction:
    def __init__(self, nr: int, dr = 1):
        assert dr != 0, f"Numerator cannot equal to zero!"
                
        if nr < 0 and dr <0:
            self.nr, self.dr = self.__reduce(-nr, -dr)
        else:
            self.nr, self.dr = self.__reduce(nr, dr)
            
    def show(self):
        print(f"{self.nr}/{self.dr}")
        
    @staticmethod
    def HighestCommonFractor(x: int, y: int):
        if y == 0: return x
        return Fraction.HighestCommonFractor(y, x % y)
    
    def __reduce(self, x , y):
        gcd = self.HighestCommonFractor(x, y)
        return int(x / gcd), int(y / gcd)
    
    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        nr = self.nr*other.dr + self.dr*other.nr
        dr = self.dr*other.dr
        return Fraction(nr, dr)
    
    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        nr = self.nr*other.dr - self.dr*other.nr
        dr = self.dr*other.dr
        return Fraction(nr, dr)
    
    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        nr = self.nr*other.nr
        dr = self.dr*other.dr
        return Fraction(nr, dr)
    
    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        nr = self.nr*other.dr
        dr = self.dr*other.nr
        return Fraction(nr, dr)
        
f1 = Fraction(-3,0)
f2 = Fraction(-1,5)
f3 = f1 + 5
f4 = f1 - 2
f5 = f1 * f2
f6 = f1 / f2
f3.show()
f4.show()
f5.show()
f6.show()