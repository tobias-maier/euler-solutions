"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?
"""

exponent = 1000
s = sum(int(d) for d in str(2 ** exponent))
print(s)