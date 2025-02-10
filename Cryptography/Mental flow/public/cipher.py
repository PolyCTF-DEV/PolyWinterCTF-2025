import numpy as np
import random

class Cipher:
    def __init__(self, polynom, seed=None):
        self.seed = seed if seed else self.generate_seed()
        self.state = np.array(self.seed, dtype=np.uint8)
        
        if any(t >= len(self.seed) for t in polynom):
            raise ValueError(f"Error: the index in the polynomial is out of bounds (maximum {len(self.seed) - 1})")
        
        self.polynom = np.array(polynom, dtype=np.uint8)


    def step(self):
        feedback = np.bitwise_xor.reduce(self.state[self.polynom])
        output = self.state[-1]
        self.state[1:] = self.state[:-1]
        self.state[0] = feedback
        return output


    def generate_keystream(self, length):
        return [self.step() for _ in range(length)]
    
    
    def generate_seed(self, size=32):
        return [random.randint(0, 1) for _ in range(size)]


    def text_to_bits(self, text):
        return [int(b) for char in text for b in format(ord(char), '08b')]


    def bits_to_hex(self, bits):
        hex_str = hex(int(''.join(map(str, bits)), 2))[2:]
        return hex_str.zfill(len(bits) // 4)


    def xor_bits(self, data_bits, keystream):
        return [data_bits[i] ^ keystream[i] for i in range(len(data_bits))]


    def encrypt(self, text):
        data_bits = self.text_to_bits(text)
        keystream = self.generate_keystream(len(data_bits))
        encrypted_bits = self.xor_bits(data_bits, keystream)
        return self.bits_to_hex(encrypted_bits)
