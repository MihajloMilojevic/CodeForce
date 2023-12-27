def case():
    n = int(input())
    a = [int(x) for x in input().split()]
    par = len([x for x in a if x % 2 == 0])
    nepar = len([x for x in a if x % 2 != 0])
    if par % 2 == 0 and nepar % 2 == 0:
        return "YES"
    if (par % 2 + nepar % 2) % 2 != 0:
        return "NO"
    s = set(a)
    for x in s:
        if (x+1) in s or (x-1) in s:
            return "YES"
    return "NO"


t = int(input())
rez = []

while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)