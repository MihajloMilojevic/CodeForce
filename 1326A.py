
def case():
    n = int(input())
    if n == 1:
        return -1
    if n == 2:
        return 23
    if (n-1) % 3 != 0:
        return "2"*(n-1) + "3"
    return "2" * (n-2) + "33"

t = int(input())
rez = []

while t:
    t-=1
    rez.append(case())

for r in rez:
    print(r)