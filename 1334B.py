def case():
    n, x = [int(x) for x in input().split()]
    a = sorted([int(x) for x in input().split()])
    s = sum(a)
    i = 0
    res = 0
    while i < n:
        if a[i] >= x:
            res = max(res, n-i)
            break
        if s / (n-i) >= x:
            res = max(res, n-i)
            break
        s -= a[i]
        i += 1
    return res


t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)