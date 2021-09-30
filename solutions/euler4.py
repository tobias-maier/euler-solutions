"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

from utils.predicates import is_palindrome

lower = 100
upper = 1000
palindromes = {i * j for i in range(lower, upper) for j in range(lower, upper) if is_palindrome(i * j)}
print(max(palindromes))