"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII
(American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42,
and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a
given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key
on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of
random bytes. The user would keep the encrypted message and the encryption key in different locations, and
without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout
the message. The balance for this method is using a sufficiently long password key for security, but short
enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters.
Using p059_cipher.txt (right click and 'Save Link/Target As...'),
a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words,
decrypt the message and find the sum of the ASCII values in the original text.
"""
space = 32
words = {'and', 'or', 'the', 'that', 'man', 'house', 'get', 'got', 'will', 'it', 'woman', 'year', 'dog',
         'garden', 'ground', 'door', 'this', 'day', 'one', 'day', 'a', 'cat', 'computer', 'letter', 'word',
         'boy', 'girl', 'heart', 'body', 'money', 'tree', 'make', 'made', 'had', 'not', 'can', 'could', 'run', 'at', 'as',
         'nice', 'middle', 'sun', 'moon', 'today', 'give', 'me', 'you', 'we', 'they', 'she', 'he', 'family', 'here',
         'child', 'node', 'to', 'its', 'in', 'by', 'of', 'also', 'where', 'there', 'message', 'find', 'value', 'on', 'off',
         'enough', 'short', 'large', 'big', 'key', 'but', 'than', 'what', 'is', 'taken', 'from', 'my', 'each', 'text'}


def decrypt(text, key):
    ascii_text = (ord(c) for c in text)
    ascii_key = [ord(c) for c in key]
    return [x[0] ^ x[1] for x in zip(ascii_text, ascii_key * len(text))]


def encrypt(cipher, key):
    ascii_key = [ord(c) for c in key]
    return [x[0] ^ x[1] for x in zip(cipher, ascii_key * len(cipher))]


def decode(ascii_codes):
    return ''.join([chr(c) for c in ascii_codes])


decryped_text = [int(c) for c in open('../resources/p059_cipher.txt', 'r').read().split(',')]

keys = [chr(a) + chr(b) + chr(c) for a in range(97, 123) for b in range(97, 123) for c in range(97, 123)]

best_match = (0, '')
for key in keys:
    candidate = encrypt(decryped_text, key)
    if candidate.count(space) < 10:
        continue
    text_candidate = decode(candidate)
    matches = len(set(text_candidate.split()) & words)
    if matches > best_match[0]:
        best_match = (matches, text_candidate)

s = sum(ord(c) for c in best_match[1])
print(s)



