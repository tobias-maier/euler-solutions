"""
The sum of the squares of the first ten natural numbers is,
The square of the sum of the first ten natural numbers is,
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

limit = 100

difference = sum(range(1, limit +1))**2 - sum([i**2 for i in range(1, limit + 1)])
print(difference)