def alphabetical_value(s):
    """
    Computes the alphabetical value of the given string
    :param s: string
    :return: the value of the string
    """
    return sum([ord(c) - ord('A') + 1 for c in s])

def is_palindrom(s):
    for i in range(0, len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True
