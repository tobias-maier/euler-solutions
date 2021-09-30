# Euler 1 https://projecteuler.net/problem=1
# if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_of_multiples(upto):
    """
    Computes the sum using list comprehension
    :param upto: upper limit
    :return: sum of all numbers belo upto that are multiples of 3 or 5
    """
    return sum([i for i in range(upto) if i % 3 == 0 or i % 5 == 0])


print(sum_of_multiples(10))
print(sum_of_multiples(1000))
