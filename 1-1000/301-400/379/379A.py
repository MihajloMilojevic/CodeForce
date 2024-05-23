a, b = [int(x) for x in input().split(" ")]
h = 0
o = 0
while a:
    h += a
    uk = a + o
    o = uk % b
    a = uk // b

print(h)