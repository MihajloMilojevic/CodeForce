n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = sorted([a[i] - b[i] for i in range(n)])
j = 0
res = 0
for i in range(n):
    if c[i] <= 0:
        continue
    while j < n and c[j] <= -c[i]+1:
        j += 1
    j -= 1
    res += i - j

print(res)