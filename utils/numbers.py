from collections import deque
from math import sqrt

def proper_divisors(n):
    """
    returns a list of all proper divisors of the given number n
    """
    return [m for m in range(1, n // 2 + 1) if n % m == 0]


def is_abundant(n):
    """
    returns, if the given number is abundant, namely the sum of all
    proper divisors is greater than the given number.
    """
    return n < sum(proper_divisors(n))


def rotations(n):
    """
    returns all rotations of the digits of the given number.

    For example 347 -> 734,473
    """
    rots = []
    d = deque(str(n))
    for _ in range(0, len(str(n))):
        rots.append(int(''.join(d)))
        d.rotate()
    return rots


def is_pandigital(digits, grade=9):
    if len(str(digits)) != grade:
        return False
    return set(range(1, grade + 1)).issubset(set(map(int, str(digits))))


def unique_digital(iter):
    for v in iter:
        strv = str(v)
        if len(set(strv)) == len(strv):
            yield v


def champernowne_seq(length):
    seq = []
    counter = 1
    while len(seq) < length:
        seq.append(str(counter))
        counter += 1
    return ''.join(seq)


def is_triangle_number(n):
    return (sqrt(2 * n + 0.25) - 0.5).is_integer()


def triangle_number(n):
    return n * (n + 1) // 2


def pentagonal_number(n):
    return n * (3 * n - 1) // 2


def hexagonal_number(n):
    return n * (2 * n - 1)