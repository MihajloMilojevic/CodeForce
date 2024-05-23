n = int(input())
c = sorted([int(x) for x in input().split(" ")])
c.reverse()
s = sum(c)
cs = 0
nc = 0
while cs <= s:
    cs += c[nc]
    s -= c[nc]
    nc += 1
print(nc)