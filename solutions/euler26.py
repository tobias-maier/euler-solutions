from math import floor


def decimal_digits(n):
    nominator = 10
    fraction_digits = []
    r = []
    c_length = 0
    while nominator != 0 and c_length == 0:
        d = floor(nominator / n)
        fraction_digits.append(d)
        nominator = 10 * (nominator - d * n)
        c_length = cycle_length(fraction_digits)
    if c_length == 0:
        fraction_digits.extend(r)
        return ''.join(map(str, fraction_digits))
    else:
        return 'r' + ''.join(map(str, fraction_digits[:-c_length]))


def cycle_length(digits):
    for i in range(1, int(len(digits)/2) + 1):
        if digits[-i:] == digits[-2 * i: -i] and set(digits[-i:]) != {0}:
            return i
    return 0


max_lenght = 0
index_of_max_lenght = -1
for i in range(2, 1001):
    reciprocal = decimal_digits(i)
    print(f"1/{i}={reciprocal} --> {len(reciprocal) - 1}")
    if reciprocal.startswith("r") and len(reciprocal) - 1 > max_lenght:
        max_lenght = len(reciprocal) - 1
        index_of_max_lenght = i

print(f"l({index_of_max_lenght})={max_lenght}")
