"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def d(n):
    """sum of all proper divisors"""
    sum = 0
    for i in divisors(n):
        sum += i
    return sum


def divisors(n):
    """list of all proper divisors of n"""
    divs = [1]
    for i in range(2, n):
        if n%i == 0:
            divs.append(i)
    return divs


def calculate_d(upto):
    table_of_d = {}
    for n in range(1, upto):
        table_of_d[n] = d(n)
    return table_of_d


def amicable_numbers(upto):
    amicables = set()
    candidates = calculate_d(upto)
    for a in candidates.keys():
        if candidates[a] != a and candidates[a] < len(candidates) and candidates[candidates[a]] == a:
            if (candidates[a], a) not in amicables:
                amicables.add((a, candidates[a]))
    return amicables


def sum_of_amicables(upto):
    sum = 0
    for t in amicable_numbers(upto):
        sum += t[0] + t[1]
    return sum


print(sum_of_amicables(10000))