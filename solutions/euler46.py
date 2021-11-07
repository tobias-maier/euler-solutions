"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
from utils.primes import primes
from utils.primes import goldbach_decomposition


limit = 1_000_000
p_set = set(primes(limit))

for n in range(9, limit, 2):
    if n in p_set:
        continue
    goldbach_decomposition(n)
