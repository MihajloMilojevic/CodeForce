def case():
    a = [int(x) for x in input().split()]
    for x in a:
        if a.count(x) == 1:
            return x
    return 0

t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)