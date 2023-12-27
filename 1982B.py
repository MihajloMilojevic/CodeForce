def case():
    n = int(input())
    a = [int(x) for x in input().split()]
    r = 0
    for x in a:
        if x != 1:
            break
        r += 1
    if r == n:          # all 1
        return ["First", "Second"][(r+1)%2]
    return ["First", "Second"][r%2]

t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)