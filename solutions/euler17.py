"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

base_numbers_to_words = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}


def number_to_word(i):
    if i <= 20:
        return base_numbers_to_words[i]
    elif i < 100:
        return '{0}-{1}'.format(base_numbers_to_words[i // 10 * 10], base_numbers_to_words[i % 10])
    elif i % 100 == 0 and i < 1000:
        return '{} hundred'.format(base_numbers_to_words[i // 100])
    elif i < 1000:
        hundred_digit = i // 100
        return '{} hundred and {}'.format(base_numbers_to_words[hundred_digit], number_to_word(i % 100))
    elif i == 1000:
        return 'one {}'.format(base_numbers_to_words[1000])
    return ''


words = [number_to_word(i) for i in range(1, 1001)]
s = sum([len(word.replace(' ', '').replace('-', '')) for word in words])
print(s)