import os
import random
from Crypto.Util.strxor import strxor

def read_file(filepath):
    with open(filepath, 'rb') as f:
        return f.read()

def generate_key(size):
    return os.urandom(size)

def repeat_data(data, factor):
    return data * factor

def encrypt(data, key):
    return strxor(data, key)

def write_file(filepath, content):
    with open(filepath, 'w') as f:
        f.write(content.hex())

if __name__ == "__main__":
    input_data = read_file('input.txt')
    key_size = random.randint(12, 44)
    encryption_key = generate_key(key_size)
    expanded_key = repeat_data(encryption_key, len(input_data))
    expanded_data = repeat_data(input_data, key_size)
    encrypted_text = encrypt(expanded_data, expanded_key)
    write_file('output.txt', encrypted_text)
