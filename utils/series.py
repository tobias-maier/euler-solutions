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
