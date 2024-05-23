import bisect

def case():
    n, q = [int(x) for x in input().split()]
    a = reversed(sorted([int(x) for x in input().split()]))
    b = [0]
    for x in a:
        b.append(x + b[-1])
    res = []
    # print(b)
    for i in range(q):
        x = int(input())
        if x > b[-1]:
            res.append("-1")
        else:
            res.append(str(bisect.bisect_right(b, x-1)))
    # print(res)
    return res

t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print("\n".join(r))