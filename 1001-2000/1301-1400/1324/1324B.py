def case():
    n = int(input())
    a = [int(x) for x in input().split()]
    appears = {}
    for i in range(n):
        if a[i] not in appears:
            appears[a[i]] = i
            continue
        if appears[a[i]] == i-1:
            continue
        return "YES"
    return "NO"

t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)