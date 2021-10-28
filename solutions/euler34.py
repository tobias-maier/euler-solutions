"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""
from math import factorial

curious_numbers = []
fact_lookup = {str(i) :factorial(i) for i in range(0, 10)}

for n in range(3, 9_999_999):
    if sum([fact_lookup[d] for d in str(n)]) == n:
        curious_numbers.append(n)
print(sum(curious_numbers))