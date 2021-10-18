"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

size = 1001
spiral = [[0] * size for _ in range(size)]
r = size // 2
c = size // 2
spiral[r][c] = 1
direction = 'r'
counter = 2
while counter <= size ** 2:
    if direction == 'r':
        c += 1
        if r < size - 1 and spiral[r+1][c] == 0:
            direction = 'd'
    elif direction == 'd':
        r += 1
        if c > 0 and spiral[r][c-1] == 0:
            direction = 'l'
    elif direction == 'u':
        r -= 1
        if c < size - 1 and spiral[r][c+1] == 0:
            direction = 'r'
    elif direction == 'l':
        c -= 1
        if r > 0 and spiral[r-1][c] == 0:
            direction = 'u'
    spiral[r][c] = counter
    counter += 1

s = sum({spiral[i][i] for i in range(size)} | {spiral[i][size - i - 1] for i in range(size)})
print(s)
