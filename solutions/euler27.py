"""
Euler discovered the remarkable quadratic formula: n^2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n < 40

The incredible formula n^2 - 79n + 1601  was discovered, which produces 80 primes for the consecutive values.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
n^2 + an + b where |a| < 1000 and |b| <= 1000

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number
of primes for consecutive values of , starting with n = 0.
"""
from utils.primes import is_prime

def consecutive_primes(f):
    n = 0
    while is_prime(f(n)):
        n += 1
    return n

ma, mb = -999, -1000
m_consectutives = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        consec_primes = consecutive_primes(lambda n: n**2 + a * n + b)
        if consec_primes > m_consectutives:
            m_consectutives = consec_primes
            ma, mb = a, b

print(ma, mb, m_consectutives)