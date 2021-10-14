def proper_divisors(n):
    """
    returns a list of all proper divisors of the given number n
    """
    return [m for m in range(1, n // 2 + 1) if n % m == 0]


def is_abundant(n):
    """
    returns, if the given number is abundant, namely the sum of all
    proper divisors is greater than the given number.
    """
    return n < sum(proper_divisors(n))
