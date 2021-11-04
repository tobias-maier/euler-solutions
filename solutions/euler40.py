"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.
d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
from utils.numbers import champernowne_seq
from math import prod

seq = champernowne_seq(1_000_000)
product = prod(int(seq[i]) for i in [0, 9, 99, 999, 9_999, 99_999, 999_999])
print(product)
