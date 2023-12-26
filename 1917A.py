def case():
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    if 0 in a:
        return 0
    neg = len([x for x in a if x < 0])
    if neg % 2 == 0:
        return 1
    return 0


t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)
    if r > 0:
        print("1 0")