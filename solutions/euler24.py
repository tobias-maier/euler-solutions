import math


def permutations(perms, n):
    extended_perms = []
    for p in perms:
        extended_perms += [p[:i] + [n] + p[i:] for i in range(0, len(p) + 1)]
    if n == 0:
        return extended_perms
    else:
        return permutations(extended_perms, n-1)


perms = permutations([[]], 9)
perms.sort()
print(len(perms))
print(math.factorial(10))
print(''.join(map(str, perms[999999])))