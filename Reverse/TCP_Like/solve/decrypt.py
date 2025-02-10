import random

# Функция побитовых операций (аналог bitwise)
def bitwise(a1, a2, a3):
    v3 = (3 * a2 + ord(a1)) % 3
    if v3 == 2:
        v5 = chr(a3 | ord(a1))
    elif v3 == 1:
        v5 = chr(a3 ^ ord(a1))
    else:
        v5 = chr(a3 & ord(a1))

    v6 = ord(v5) % 94 + 33
    if v6 == 32:
        return chr(95)
    return chr(v6)



def encode(s):
    result = []
    for i in range(len(s)):
        char = s[i]
        if i % 2 == 0:
            char = bitwise(char, i, 37)
            char = bitwise(char, i + 1, 34)
            char = bitwise(char, i + 2, 2)
        if i % 3 == 0:
            char = bitwise(char, i, 3)
            char = bitwise(char, i + 1, 7)
            char = bitwise(char, i + 2, 69)
        if i % 4 == 0:
            char = chr(ord(char) + 8)
            char = bitwise(char, i, 3)
        if i % 5 == 0:
            char = bitwise(char, i, 4)
            char = bitwise(char, i + 1, 6)

        if i == 6:
            char = bitwise(char, 6, 16)
            char = bitwise(char, 7, 32)
        elif i == 7:
            char = bitwise(char, 7, 5)
        elif i == 8:
            char = chr(ord(char) + 1)
            char = bitwise(char, 8, 3)
        elif i == 9:
            char = bitwise(char, 9, 2)
            char = bitwise(char, 10, 1)
        elif i == 10:
            char = bitwise(char, 10, 8)
        elif i == 11:
            char = bitwise(char, 11, 4)
            char = bitwise(char, 12, 2)
        elif i == 12:
            char = bitwise(char, 12, 6)
            char = bitwise(char, 13, 16)
        elif i == 13:
            char = bitwise(char, 13, 91)
            char = bitwise(char, 14, 7)
        elif i == 15:
            char = bitwise(char, 15, 4)
            char = bitwise(char, 16, 107)
        elif i == 16:
            char = bitwise(char, 16, 8)
            char = bitwise(char, 17, 5)

        result.append(char)
    return ''.join(result)



def main():
    random_string = "OuGBsX9w4FWBkqSK"
    encoded_string = encode(random_string)
    print(encoded_string)



if __name__ == "__main__":
    main()
