from cipher import *


numbers = input("Enter the secret numbers: ").split()
polynom = [int(num) for num in numbers]
flag = "PolyCTF{eto_ne_flag}"

cipher = Cipher(polynom)
ciphertext = cipher.encrypt(flag)

with open('output.txt', 'w') as file:
    file.write(f"seed: {cipher.seed}\n")
    file.write(f"Encrypted: {ciphertext}")

