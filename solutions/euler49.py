"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
from itertools import permutations
from utils.primes import primes

fixed_digit_primes = set(filter(lambda n: 1000 <= n <= 9999, primes(10_000)))
for p in fixed_digit_primes:
    candidates = sorted(list({int(''.join(pn)) for pn in permutations(str(p)) if int(''.join(pn)) in fixed_digit_primes}))
    if len(candidates) <= 2:
        continue
    distances = [candidates[i+1] - candidates[i] for i in range(len(candidates) - 1)]
    print(candidates, distances)


