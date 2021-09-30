from math import sqrt
from math import floor


def eratosthenes(upto):
    """
    algorithm of eratosthenes for finding all prime numbers up to the given limit.

    :param upto: upper limit
    :return: list of all prime numbers less than the given limit
    """
    candidates = [True] * upto
    i = 2
    while i < sqrt(upto):
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
    for divisor in eratosthenes(floor(sqrt(n)) + 1):
        while remainder % divisor == 0:
            factors.append(divisor)
            remainder //= divisor
    if remainder > 1:
        factors.append(remainder)
    return factors
