"""
There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345


How many, not necessarily distinct, values of
for , are greater than one-million?
"""
from math import comb

million_exceeds = 0
for n in range(1, 101):
    for r in range(1, n+1):
        if comb(n, r) > 1_000_000:
            million_exceeds += 1
print(million_exceeds)