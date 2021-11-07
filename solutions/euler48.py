"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""
s = sum(n**n for n in range(1, 1001))
print(str(s)[-10:])