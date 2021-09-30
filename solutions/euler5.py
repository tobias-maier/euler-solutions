"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import utils.primes as p

limit = 20
factors = [p.factorize(n) for n in range(2, limit + 1)]
product = 1
for prime in p.eratosthenes(limit + 1):
    product *= prime ** max([c.count(prime) for c in factors])

print(product)
