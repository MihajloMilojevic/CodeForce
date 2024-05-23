def case():
    n = int(input())
    a = [int(x) for x in input().split()]
    par = len([x for x in a if x % 2 == 0])
    if par == 0 or par == n:
        return "YES"
    return "NO"

t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)