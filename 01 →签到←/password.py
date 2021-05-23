# Author: Xzonn
# Date: 2021-05-23

a = "synt{J3ypbzr gb 0gu CXH ThThTh, rawbl gur tnzr!}"
b = ""
for i in a:
    if "a" <= i <= "z":
        i = chr((ord(i) - ord("a") + ord("f") - ord("s") + 26) % 26 + ord("a"))
        b += i
    elif "A" <= i <= "Z":
        i = chr((ord(i) - ord("A") + ord("f") - ord("s") + 26) % 26 + ord("A"))
        b += i
    else:
        b += i
print(b)