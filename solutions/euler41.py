"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from utils.primes import primes
from utils.numbers import is_pandigital

for p in reversed(primes(9_999_999)):
    if is_pandigital(p, len(str(p))):
        print(p)
        break

