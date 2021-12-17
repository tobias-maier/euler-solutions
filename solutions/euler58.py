"""

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side
length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal,
but what is more interesting is that 8 out of the 13 numbers lying along both diagonals
are prime; that is, a ratio of 8/13 ≈ 62%.
If one complete new layer is wrapped around the spiral above, a square spiral with side
length 9 will be formed. If this process is continued, what is the side length of the
square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""
from utils.primes import primes

limit = 413_000_000
prime_set = set(primes(limit))

diagonal_primes_count = 0
size = 3
while True:
    if (size**2) > limit:
        limit = int(limit * 1.2)
        print('recalc prime set with new limit ' + str(limit))
        prime_set = set(primes(limit))
    d = (size-2)**2
    if (d + (size - 1)) in prime_set:
        diagonal_primes_count += 1
    if size**2 in prime_set:
        diagonal_primes_count += 1
    if (d + 3*(size - 1)) in prime_set:
        diagonal_primes_count += 1
    if (d + 2*(size - 1)) in prime_set:
        diagonal_primes_count += 1
    diagonal_prime_ration = diagonal_primes_count / (2 * size - 1)
    print(size, diagonal_prime_ration)
    size += 2
    if diagonal_prime_ration < 0.1:
        break

