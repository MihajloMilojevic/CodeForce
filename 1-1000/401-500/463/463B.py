n = int(input())
h = [int(x) for x in input().split()]
res = -h[0]
tr = -h[0]
for i in range(n-1):
    tr += h[i] - h[i+1]
    res = min(res, tr)

print(-res)