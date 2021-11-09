"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
from utils.primes import primes

upto = 1_000_000
prime_list = list(filter(lambda n: n <= upto, primes(upto)))
prime_set = set(prime_list)

max_sum = 2
max_length = 1
for start in range(len(prime_list)):
    for end in range(start + 1, len(prime_list)):
        s = sum(prime_list[n] for n in range(start, end))
        if s >= upto:
            break
        if s in prime_set:
            if max_length < end - start:
                max_sum = s
                max_length = end - start
print(max_sum, max_length)

