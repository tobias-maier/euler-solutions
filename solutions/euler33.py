"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify
it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value,
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
from fractions import Fraction
from math import prod

candidates = [(str(n), str(d)) for n in range(10, 100) for d in range(n+1, 100)]
found = []
for d, n in candidates:
    f = Fraction(int(d), int(n))
    if d[0] != '0' and d[0] == n[0] and n[1] != '0' and f == Fraction(int(d[1]), int(n[1])):
        found.append((d, n))
    elif d[0] != '0' and d[0] == n[1] and n[0] != '0' and f == Fraction(int(d[1]), int(n[0])):
        found.append((d, n))
    elif d[1] != '0' and d[1] == n[0] and n[1] != '0' and f == Fraction(int(d[0]), int(n[1])):
        found.append((d, n))
    elif d[1] != '0' and d[1] == n[1] and n[0] != '0' and f == Fraction(int(d[0]), int(n[0])):
        found.append((d, n))
s = prod([Fraction(int(d), int(n)) for d, n in found])
print(s)