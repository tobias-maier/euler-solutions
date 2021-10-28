"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
from utils.strings import is_palindrom

s = sum([n for n in range(1, 1_000_000) if is_palindrom(str(n)) and is_palindrom(format(n, 'b'))])
print(s)