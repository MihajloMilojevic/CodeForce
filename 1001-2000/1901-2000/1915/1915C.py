import math

def case():
    n = int(input())
    a = [int(x) for x in input().split()]
    s = sum(a)
    sq = int(math.sqrt(s))
    if sq ** 2 == s:
        return "YES"
    else:
        return "NO"

t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)