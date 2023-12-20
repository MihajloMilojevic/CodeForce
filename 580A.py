n = int(input())
a = [int(x) for x in input().split(" ")]
m = 0
c = 1
for i in range(1, n):
    if a[i] < a[i-1]:
        m = max(m, c)
        c = 0
    c += 1
m = max(m, c)
print(m)