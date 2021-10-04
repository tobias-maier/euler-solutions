"""
tarting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""

routes = {}


def number_of_routes(i, j):
    global routes
    if i == 0 or j == 0:
        return 1
    if (i - 1, j) not in routes:
        routes[(i - 1, j)] = number_of_routes(i - 1, j)
    if (i, j - 1) not in routes:
        routes[(i, j - 1)] = number_of_routes(i, j - 1)
    return routes[(i - 1, j)] + routes[(i, j - 1)]


print(number_of_routes(20, 20))