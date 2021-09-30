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


print(amicable_numbers(10000))
print(sum_of_amicables(10000))