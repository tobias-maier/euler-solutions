"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
import itertools

def is_pandigital(s):
    if len(s) != 9 or '0' in s:
        return False
    return len(set(s)) == 9

base = list(map(str, range(1,10)))
p = [(e[0:2], e[2:5], int(e[0:2]) * int(e[2:5])) for e in list(map(lambda s: ''.join(s), itertools.permutations(base, 5)))
     if is_pandigital(e[0:2] + e[2:5] + str(int(e[0:2]) * int(e[2:5])))]
q= [(e[0], e[1:5], int(e[0]) * int(e[1:5])) for e in list(map(lambda s: ''.join(s), itertools.permutations(base, 5)))
     if is_pandigital(e[0] + e[1:5] + str(int(e[0]) * int(e[1:5])))]

s = sum({e[2] for e in p + q})
print(s)
