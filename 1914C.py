def case():
    parts = input().split(" ")
    n = int(parts[0])
    k = int(parts[1])
    a = [int(x) for x in input().split(" ")]
    b = [int(x) for x in input().split(" ")]
    rez = 0
    bmax = 0
    asum = 0
    i = 0
    while i < k and i < n:
        asum += a[i]
        bmax = max(bmax, b[i])
        rez = max(rez, asum + (k-i-1)*bmax)
        i += 1
    return rez






t = int(input())
rez = []
while t:
    rez.append(case())
    t -= 1

for r in rez:
    print(r)
