def alphabetical_value(s):
    """
    Computes the alphabetical value of the given string
    :param s: string
    :return: the value of the string
    """
    return sum([ord(c) - ord('A') + 1 for c in s])
