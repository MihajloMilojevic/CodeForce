def case():
    a, b = [int(x) for x in input().split()]
    return "Bob" if (a + b) % 2 == 0 else "Alice"

t = int(input())
rez = []
while t:
    t-=1
    rez.append(case())

for r in rez:
    print(r)