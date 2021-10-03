def fib(upto_predicate):
    """
    computes a list of fibonacci numbers
    :param upto_predicate: predicate function with arguments index and current value
    :return: list of fibonacci numbers fulfilling the given predicate
    """
    current_value, next_value = 1, 2
    numbers = [current_value]
    index = 1
    while upto_predicate(index+1, next_value):
        current_value, next_value = next_value, current_value + next_value
        numbers.append(current_value)
        index += 1
    return numbers


def triangle_numbers(upto):
    """
    computes a sequence of all triangle numbers with length upto. The n-th triangle number is the sum
    1 + 2 + 3 + ... + n
    :param upto: the uppber bound
    :return: a list of all triangle numbers below upto
    """
    return [n * (n + 1) // 2 for n in range(1, upto)]


def collatz_sequence(start):
    n = start
    seq = []
    while n > 1:
        seq.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    seq.append(1)
    return seq
