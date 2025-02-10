from berlekamp_massey import *
from cipher import *

def xor_bytes(data: bytes, key: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(data, key))

known_cleartext = "PolyCTF{"
ciphertext = bytes.fromhex("871366cbb4e5c9286ed1e6b1b2e5bdbe79ed0e0a7d08dd345d87c8f4f6943f6928a141714e816a52da59808af455b3eec966a7facfe6c262b26a13f823e44f15256d14d0953a0707c6b6055a78f8294f18632fc8")

bitstream = xor_bytes(known_cleartext.encode(), ciphertext[:len(known_cleartext)])

bit_sequence = [int(b) for byte in bitstream for b in format(byte, '08b')]

bm = BerlekampMassey(bit_sequence)

print("Recovered LFSR polynomial:", bm)
print("Polynomial degree:", bm.get_polynomial_degree())
print("LFSR taps (feedback positions):", bm.get_polynomial())

polynom = []
for item in bm.get_polynomial():
    if item - 1 >= 0:
        polynom.append(item-1)
        
print(f"polynom: {polynom}")
seed = [0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1]

cipher = Cipher(polynom, seed)

keystream = bytes.fromhex(cipher.bits_to_hex(cipher.generate_keystream(len(ciphertext) * 8)))

flag = xor_bytes(keystream, ciphertext)

print(flag.decode())


