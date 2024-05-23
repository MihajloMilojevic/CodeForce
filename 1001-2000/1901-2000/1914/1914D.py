def check(a):
    return a["value"]

def is_larger(a, b, inda, indb):
    i = len(inda)
    j = len(indb)
    while i > 0 and j > 0:
        ia = inda[i-1]
        ib = indb[j-1]
        if a[ia] > b[ib]:
            return True
        if a[ia] < b[ib]:
            return False
        i -= 1
        j -= 1
    return i > j

def case():
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    b = [int(x) for x in input().split(" ")]
    c = [int(x) for x in input().split(" ")]
    ia = [x["index"] for x in reversed(sorted([{"value": a[i], "index": i} for i in range(n)], key=check))][:3]
    ib = [x["index"] for x in reversed(sorted([{"value": b[i], "index": i} for i in range(n)], key=check))][:3]
    ic = [x["index"] for x in reversed(sorted([{"value": c[i], "index": i} for i in range(n)], key=check))][:3]
    res = 0
    for i in ia:
        for j in ib:
            if i == j:
                continue
            for k in ic:
                if k == i or k == j:
                    continue
                res = max(res, a[i] + b[j] + c[k])
    return res  

t = int(input())
rez = []
while t:
    rez.append(case())
    t -= 1

for r in rez:
    print(r)
