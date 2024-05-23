def case():
    a, b, c = [int(x) for x in input().split()]
    s = a + b + c
    d = s // 9
    if s % 9 == 0 and a >= d and b >= d and c >= d:
        return "YES"
    return "NO"


t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)