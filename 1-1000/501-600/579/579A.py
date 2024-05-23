import math

x = int(input())
d = 0
while x:
    d += 1
    x -= 2 ** int(math.log2(x))

print(d)