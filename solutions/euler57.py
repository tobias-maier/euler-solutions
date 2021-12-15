"""
Square root convergents
In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
"""
from fractions import Fraction

counter = 0
d = Fraction(2)
for i in range(0, 1000):
    n = Fraction(1) + Fraction(1, d)
    d = Fraction(2) + Fraction(1, d)
    if len(str(n.numerator)) > len(str(d.denominator)):
        counter += 1
print(counter)
