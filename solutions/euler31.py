"""
In the United Kingdom the currency is made up of pound (£) and pence (p).
There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
v = [(p100, p50, p20, p10, p5, p2, 200 - p100 * 100 - p50 * 50 - p20 * 20 - p10 * 10 - p5 * 5 - p2 * 2)
     for p100 in [0, 1, 2] for p50 in range(5) for p20 in range(11) for p10 in range(21) for p5 in range(41) for p2 in range(101)
     if 200 - p100 * 100 - p50 * 50 - p20 * 20 - p10 * 10 - p5 * 5 - p2 * 2 >= 0]
print(len(v) + 1)