def case():
    n = int(input())
    a = [int(x) for x in input().split()]
    i = n - 1
    rez = a[-1]
    while i >= 0:
        if i + a[i] < n:
            a[i] = a[i] + a[i + a[i]]
        if a[i] > rez:
            rez = a[i]
        i -= 1
    return rez
    

t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())
for r in rez:
    print(r)