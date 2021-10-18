"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

p = 5
def sum_of_power_digits(number, power=p):
    return sum([int(d) ** power for d in str(number)])


s = sum({n for n in range(2, 5*9**p) if sum_of_power_digits(n) == n})
print(s)
