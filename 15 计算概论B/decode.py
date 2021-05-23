# Author: Xzonn
# Date: 2021-05-23

import json

with open("result.txt") as f:
    result = f.read()

with open('table.json') as f:
    table = json.load(f)
d = {v:k for k,v in table}
print(d)
r = ''
tmp = ''
for c in result:
    tmp += c
    if tmp in d:
        r += d[tmp]
        tmp = ''
assert tmp == ''

with open("text.txt", "w") as f:
    f.write(r[::-1])