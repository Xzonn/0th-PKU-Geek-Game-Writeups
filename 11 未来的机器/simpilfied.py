# Author: Xzonn
# Date: 2021-05-23

import struct

m1152 = [0 for i in range(96)]
m1552 = [0 for i in range(96)]
m1952 = [0 for i in range(96)]
m2336 = [0 for i in range(96)]
key = '.q~03QKLNSp"s6AQtEW<=MNv9(ZMYntg2N9hSe5=k'.encode()
key_len = len(key)
fla = 'flag{123456789abcdefghijklmnopqrstuvwxyz}'.encode()
fla_len = len(fla)
pos = 0
seed = 114514

for pos in range(0, 96):
    m1952[pos] = pos

for pos in range(1, 96):
    seed = ((seed * 1919 + 7) % 334363) & -1
    v113 = (seed % pos) & -1
    m1952[v113], m1952[pos] = m1952[pos], m1952[v113]

for pos in range(0, fla_len):
    if fla[pos] < 32 or fla[pos] >= 128:
        raise ValueError("包含不可打印的 ASCII 字符：\\" + hex(fla[pos])[1:])
    m1152[pos] = (((m1952[fla[pos] - 32] + pos) % 96 ) & -1) + 32

for pos in range(0, fla_len):
    m2336[pos] = pos

for pos in range(1, fla_len):
    seed = ((seed * 1919 + 7) % 334363) & -1
    v113 = (seed % pos) & -1
    m2336[v113], m2336[pos] = m2336[pos], m2336[v113]

for pos in range(0, fla_len):
    m1552[m2336[pos]] = m1152[pos]

for pos in range(0, fla_len):
    m1552[pos] = key[pos]

for pos in range(0, fla_len):
    m1152[pos] = m1552[m2336[pos]]

n_fla = ""
for pos in range(0, fla_len):
    n_fla += chr(m1952.index((m1152[pos] - 32 - pos + 96) % 96) + 32)

print(n_fla)