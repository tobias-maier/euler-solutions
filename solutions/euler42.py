"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its alphabetical position and adding these v
alues we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
If the word value is a triangle number then we shall call the word a triangle word.
Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand 
common English words, how' many are triangle words?
"""
from utils.numbers import is_triangle_number


def word_value(w):
    return sum(ord(c) - ord('A') + 1 for c in w)


with open(r'../resources/words.txt', 'r') as f:
    cnt = 0;
    for word in f.read().split(','):
        if is_triangle_number(word_value(word.replace('"', ''))):
            cnt += 1

print(cnt)

