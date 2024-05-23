def case():
    n, k = [int(x) for x in input().split()]
    if k == 1:
        return 1
    if n % k == 0:
        return 1
    if k % n == 0:
        return k // n
    if k < n:
        k = n + k - n%k
    return k // n + (1 if k % n else 0)

t = int(input())
rez = []

while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)