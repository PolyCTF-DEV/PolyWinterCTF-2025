import string

def from_binart(text):
    result = []
    for i in text.split():
        result.append(chr(int(i, 2)))
    print(result)
    return "".join(result)

def atbash(text):
    print(text)
    alphabet = string.ascii_uppercase + string.ascii_lowercase
    reversed_alphabet = alphabet[::-1]
    table = str.maketrans(alphabet + string.digits + string.punctuation,
                          reversed_alphabet + string.digits[::-1] + string.punctuation[::-1])
    return text.translate(table)


def reverse_text(text):
    print(text)
    return text[::-1]


def rot13(text):
    print(text)
    result = []
    for i in text:
        char = ord(i) + 13
        if char > 126:
            char =- 95
        result.append(char)
    return result

def xor(text):
    result = []
    print(text)
    for i in text:
        result.append(chr(i ^ 8))
    return "".join(result)

text = "01010011 01011011 01011011 01011011 00111101 01001101 01001110 00100101 01001010 00111101 01101110 01110001 01100010 00111111 01110001 01000000 01001100 01010000 01110111 01001110 00101101 01010101 01111010 01101100 00101101 01010111 01100100 01100001 01110000"
print(xor(rot13(reverse_text(atbash(from_binart(text))))))
