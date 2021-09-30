def even(v):
    return v % 2 == 0


def is_palindrome(n):
    s = str(n)
    mid = len(s) // 2
    return s[:mid] == s[::-1][:mid]
