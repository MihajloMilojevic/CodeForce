p = input().split(" ")
n = int(p[0])
m = int(p[1])
f = sorted([int(x) for x in input().split(" ")])
l = 0
r = n-1
rez = f[-1] - f[0]
while r < m:
    rez = min(rez, f[r]-f[l])
    r += 1
    l += 1
print(rez)