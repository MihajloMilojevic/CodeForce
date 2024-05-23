n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
b = [int(x) for x in input().split()]
lookup = {}
for i in range(n):
    lookup[a[i]] = (i+1, n-i)

v, p = 0, 0
for x in b:
    v += lookup[x][0]
    p += lookup[x][1]

print(v,p)