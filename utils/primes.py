from math import sqrt
from math import floor
from math import prod

_prime_seq = [2]


def primes(upto):
    global _prime_seq
    if upto <= _prime_seq[-1]:
        return _prime_seq
    else:
        _prime_seq = eratosthenes(max(2 * upto, 1000))
        return _prime_seq


def is_prime(n):
    return n in primes(n)


def eratosthenes(upto):
    """
    algorithm of eratosthenes for finding all prime numbers up to the given limit.

    :param upto: upper limit
    :return: list of all prime numbers less than the given limit
    """
    candidates = [True] * upto
    i = 2
    limit = sqrt(upto)
    while i < limit:
        if candidates[i]:
            for j in range(i**2, upto, i):
                candidates[j] = False
        i += 1
    return [i for i in range(2, upto) if candidates[i]]


def factorize(n):
    """
    Factorize the given number
    :param n: number which should be factorized
    :return: list of all prime factors
    """
    factors = []
    remainder = n
    for divisor in primes(floor(sqrt(n)) + 1):
        while remainder % divisor == 0:
            factors.append(divisor)
            remainder //= divisor
    if remainder > 1:
        factors.append(remainder)
    return factors

def factorize_canonical(n):
    """
    Factorize the given number
    :param n: number which should be factorized
    :return: dictionary, with prime factor as key and multiplicity of the prime
             factor as value
    """
    factors = {}
    remainder = n
    for divisor in primes(floor(sqrt(n)) + 1):
        while remainder % divisor == 0:
            if divisor not in factors:
                factors[divisor] = 0
            factors[divisor] += 1
            remainder //= divisor
    if remainder > 1:
        if remainder not in factors:
            factors[remainder] = 0
        factors[remainder] += 1
    return factors


def factors(n):
    """
    Returns a list of all factors for the given n
    :param n: number
    :return: list of all numbers evenly divisible
    """
    return [i for i in range(1, n + 1) if n % i == 0]


def num_of_divisors(n):
    """
    Return the number of divisors of the given integer n
    The algorithm uses the formula described in
    https://en.wikipedia.org/wiki/Divisor_function
    :param n: the integer
    :return: the number of divisors
    """
    return prod([v + 1 for v in factorize_canonical(n).values()])
