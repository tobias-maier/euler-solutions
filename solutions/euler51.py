"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:
3, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having
seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
"""
from utils.primes import primes
from utils.sets import powerset


def replace_position(n, pos, replaced_digit):
    ten_power_pos = 10**pos
    ten_power_minor_pos = 10**(pos - 1)
    return n//ten_power_pos * ten_power_pos + replaced_digit * ten_power_minor_pos + n % ten_power_minor_pos


def replace_positions(n, positions, replaced_digit):
    for pos in positions:
        n = replace_position(n, pos, replaced_digit)
    return n


prime_list = primes(10_000_000)

max_family_miss = 2
family_set = []
for n in range(5, 7):
    n_length_primes = set(filter(lambda p: 10**(n-1) < p < 10**n, prime_list))
    for p in range(10**(n-1), 10**n):
        for positions in powerset(range(2, n + 1)):
            if len(positions) == 0:
                continue
            family_miss = []
            smallest_prime = -1
            for d in range(10):
                r = replace_positions(p, positions, d)
                if r not in n_length_primes:
                    family_miss.append(d)
                elif smallest_prime == -1:
                    smallest_prime = r
                if len(family_miss) > max_family_miss:
                    break
            else:
                print(smallest_prime, positions, family_miss)
                family_set.append((smallest_prime, positions, family_miss))

print(min(family_set))



