def case():
    n = int(input())
    a = [int(x) for x in input().split()]
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    repeats = {}
    for x in a:
        if x not in repeats:
            repeats[x] = 1
        else:
            repeats[x] += 1
    k, v = max(repeats.items(), key=lambda x: x[1])
    print(repeats, (k, v))
    
    return 1




t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)