n, m, k = [int(x) for x in input().split()]
x = []
for i in range(m+1):
    x.append(int(input()))
res = 0
for i in range(m):
    diff = bin(x[i] ^ x[m]).count("1")
    if diff <= k:
        res += 1

print(res)