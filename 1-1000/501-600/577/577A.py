n, x = [int(x) for x in input().split()]
count = 0
for i in range(1, n+1):
    if x % i != 0:
        continue
    if x // i > n:
        continue
    count += 1
print(count)