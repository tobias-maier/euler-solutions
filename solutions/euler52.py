"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
import sys


def digit_set(n):
    return set(str(n))


for e in range(2, 12):
    for n in range(10**e, 10**(e+1)//6):
        s = digit_set(n)
        if s != digit_set(2*n):
            continue
        elif s != digit_set(3 * n):
            continue
        elif s != digit_set(4 * n):
            continue
        elif s != digit_set(5 * n):
            continue
        elif s != digit_set(6 * n):
            continue
        print(n)
        sys.exit()