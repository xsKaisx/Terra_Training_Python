"""Fraction

* Make a class Fraction that contains two instance variables, nr and dr (nr stands for numerator and dr for denominator). Define an __init__ method that provides values for these instance variables. Make the denominator optional by providing a default argument of 1. In the __init__ method, make the denominator positive if it is negative. For example  -2/-3 should be changed to 2/3 and 2/-3 to -2/3. Write a method named show that prints numerator, then '/' and then the denominator


- Define a method named multiply that multiples two Fraction instance objects. For multiplying two fractions, you have to multiply the numerator with numerator and denominator with the denominator.
- Create a new instance object that is the product of the two fractions and return it. Write your method in such a way that it supports multiplication of a Fraction by an integer also
- Define a method named add to add two Fraction instance objects. Sum of two fractions n1/d1 and n2/d2 is (n1*d2 + n2*d1) / (d1*d2). This method should also support addition of a Fraction by an integer
- Create a function to find the highest common factor of two numbers and make it a static method
- Write a private instance method _reduce that reduces a fraction to its lowest terms. To reduce a Fraction to its lowest terms you have to divide the numerator and denominator by the highest common factor. Call this method in __init__and also call it on the resultant fraction in methods multiply and add
"""

import math


class Fraction():
    def __init__(self, nr: int, dr: int = 1) -> None:
        if dr == 0:
            print("Fraction is not valid")
        elif nr < 0 and dr < 0:
            nr = abs(nr)
            dr = abs(dr)
        elif nr > 0 and dr < 0:
            nr = 0 - nr
            dr = abs(dr)
        self.nr, self.dr = self._reduce(nr, dr)


    def display(self):
        return "{}/{}".format(self.nr, self.dr)

    def multiple(self, frac_1, frac_2):
        nr = frac_1.nr * frac_2.nr
        dr = frac_1.dr * frac_2.dr
        nr, dr = self._reduce(nr, dr)
        return "{}/{}".format(nr, dr)

    def sum(self, frac_1, frac_2):
        nr = frac_1.nr * frac_2.dr + frac_1.dr * frac_2.nr
        dr = frac_1.dr * frac_2.dr
        nr, dr = self._reduce(nr, dr)
        return "{}/{}".format(nr, dr)

    @staticmethod
    def hcf(nr, dr):
        def find_factor(number):
            if number < 0:
                number = abs(number)
            return set([i for i in range(1, number) if number % i == 0])

        factor_set_nr = find_factor(nr)
        factor_set_dr= find_factor(dr)

        if (factor_set_dr & factor_set_dr):
            result = list((factor_set_nr & factor_set_dr))
            result.sort()
            return result[-1]

    def _reduce(self, nr, dr):
        devide_num = self.hcf(nr, dr)
        print("devide",devide_num)
        # nr = nr / devide_num
        # dr = dr / devide_num
        return nr, dr



frac_1 = Fraction(9, -6)
frac_2 = Fraction(5, -9)
frac_3 = Fraction(0)
# print(frac_3._reduce(frac_1.nr, frac_1.dr).display())
print(frac_1.multiple(frac_1, frac_2))
