# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.12.3 (main, Jan 17 2025, 18:03:48) [GCC 13.3.0]
# Embedded file name: easy_reverse.py
# Compiled at: 2025-02-03 13:51:52
# Size of source mod 2**32: 990 bytes
import string

def rot13(text):
    result = []
    for i in text:
        char = i - 13
        if char < 32:
            char += 95
        result.append(chr(char))

    return "".join(result)


def atbash(text):
    alphabet = string.ascii_uppercase + string.ascii_lowercase
    reversed_alphabet = alphabet[::-1]
    table = str.maketrans(alphabet + string.digits + string.punctuation, reversed_alphabet + string.digits[::-1] + string.punctuation[::-1])
    return text.translate(table)


def to_hex(text):
    result = []
    for i in text:
        result.append(hex(ord(i)))

    return result


def xor(text):
    result = []
    for i in text:
        result.append(int(i, 16) ^ 8)

    return result


def reverse_text(text):
    return text[::-1]


def to_binary(text):
    result = []
    for i in text:
        result.append(bin(ord(i))[2:].zfill(8))

    return " ".join(result)


text = input()
print(to_binary(atbash(reverse_text(rot13(xor(to_hex(text)))))))

# okay decompiling easy_reverse.cpython-38.pyc
