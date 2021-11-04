"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
solutions = {}
for a in range(1,499):
    for b in range(a, 500):
        c = ((a ** 2 + b ** 2) ** 0.5)
        if c.is_integer() and a + b + c <= 1000:
            perimeter = int(a + b + c)
            solutions[perimeter] = solutions[perimeter] + 1 if perimeter in solutions else 1

max_perimeter = (0, 0)
for k, v in solutions.items():
    if v > max_perimeter[1]:
        max_perimeter = (k, v)

print(max_perimeter)

