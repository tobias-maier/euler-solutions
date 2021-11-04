"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits
from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from utils.primes import primes


def is_truncatable_prime(n, prime_set):
    return {int(n[i:]) for i in range(0, len(n))} | {int(n[:i]) for i in range(1, len(n))} <= prime_set


prime_numbers = set(primes(1_000_000))

s = sum([p for p in (prime_numbers - {2,3,5,7}) if is_truncatable_prime(str(p), prime_numbers)])
print(s)