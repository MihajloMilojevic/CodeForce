def case():
    n = int(input())
    a = [int(x) for x in input().split()]
    m = a[-1]
    res = 0
    for i in range(n-2, -1, -1):
        if a[i] > m:
            res += 1
        m = min(a[i], m)
    return res


t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)