import json
from collections import Counter
import binascii

# read text to be encoded
with open('text.txt') as f:
    text = f.read()
    raw_text = binascii.unhexlify(text.encode())
    with open('raw_text.txt', 'wb') as f:
        f.write(raw_text)
    # assert b'flag{' in raw_text
    text = text[::-1]


# read translation table
with open('table.json', 'r') as f:
    table = json.load(f)

# check translation table
for char1, code1 in table:
    for char2, code2 in table:
        if char1!=char2:
            assert not code1.startswith(code2)

# check char frequency
cnt = Counter()
for c in text:
    cnt[c] += 1
print(cnt)

with open('result2.txt', 'w') as f:
    f.write(text.translate({ord(k):v for k,v in table}))