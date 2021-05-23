# Author: Xzonn
# Date: 2021-05-23

import zlib
import struct
import time

t = time.time()

with open("quine.bin", "rb") as f:
    base = f.read()

try:
    with open("last.txt") as f:
        start = int(f.read())
except:
    start = 1

for i in range(start - 1, 0x100 ** 4):
    inp = base.replace(b"\xff\xff\xff\xff", struct.pack("<L", i))
    crc = zlib.crc32(inp)
    if i == crc:
        print("result:", i)
        with open("quineresult.bin", "wb") as f:
            f.write(inp)
        break
    if (time.time() - t) > 30:
        with open("last.txt", "w") as f:
            f.write(str(i))
        t = time.time()
        print("time:", t)
