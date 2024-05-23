n, t = [int(x) for x in input().split(" ")]
a = [int(x) for x in input().split(" ")]
p = [-1] * n
for i in range(len(a)):
    p[i] = a[i]+i

found = False
next = p[0]
while next > 0:
    if next == t-1:
        found = True
        break
    next = p[next]

print("YES" if found else "NO")