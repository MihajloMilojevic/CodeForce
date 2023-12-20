def case():
    parts = input().split(" ")
    n = int(parts[0])
    k = int(parts[1])
    rez = []
    i = 1
    while k:
        rez.append(i)
        i += 1
        k -= 1
    while i <= n:
        rez.append(n - k)
        i += 1
        k += 1
    return rez






t = int(input())
rez = []
while t:
    rez.append(case())
    t -= 1

for r in rez:
    print(" ".join([str(x) for x in r]))
