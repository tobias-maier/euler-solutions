"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
from utils.primes import eratosthenes

prime_index = 10001
upto = prime_index//10
primes = []
while len(primes) < prime_index:
    primes = eratosthenes(upto)
    upto *= 2

print(primes[prime_index - 1])

