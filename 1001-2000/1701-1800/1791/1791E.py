def case():
    n = int(input())
    a = [int(x) for x in input().split()]
    res = 0
    m = 100000000001
    neg = 0
    for x in a:
        res += abs(x)
        m = min(abs(x), m)
        if x < 0:
            neg += 1
    # print(a, res, m, neg)
    if neg % 2 == 0:
        return res
    else:
        return res - 2 * m

t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)