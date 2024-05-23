def case():
    x, y = [int(q) for q in input().split(" ")]
    a, b = [int(q) for q in input().split(" ")]
    b = min(b, 2*a)
    minimum = min(x, y)
    maximum = max(x, y)
    return minimum * b + (maximum - minimum) * a

t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)