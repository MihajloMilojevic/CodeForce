import math
def case():
    n = int(input())
    a_min = math.floor(math.ceil(n/2)**(1/3))
    a_max = math.ceil((n-1)**(1/3))
    for a in range(a_min, a_max+1):
        b = math.floor(max((n - a**3), 0) ** (1/3))
        if a **3 + b **3 == n:
            return "YES"
    return "NO"


t = int(input())
rez = []

while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)