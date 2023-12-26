n, k = [int(x) for x in input().split()]
h = [int(x) for x in input().split()]
l = 1
s = sum(h[:k])
res = 0
m = s
while l+k-1 < n:
    s -= h[l-1]
    s += h[l+k-1]
    if s < m:
        res = l
        m = s
    l+=1

print(res+1)