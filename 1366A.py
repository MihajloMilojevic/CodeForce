def case():
    s, d = [int(x) for x in input().split()]
    return min(s, d,s//3 + d//3 + (s%3+d%3)//3)

t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())
for r in rez:
    print(r)