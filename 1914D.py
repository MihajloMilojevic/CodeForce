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
    ia = [x["index"] for x in sorted([{"value": a[i], "index": i} for i in range(n)], key=check)]
    ib = [x["index"] for x in sorted([{"value": b[i], "index": i} for i in range(n)], key=check)]
    ic = [x["index"] for x in sorted([{"value": c[i], "index": i} for i in range(n)], key=check)]
    print([(x["index"], x["value"]) for x in sorted([{"value": a[i], "index": i} for i in range(n)], key=check)])
    print([(x["index"], x["value"]) for x in sorted([{"value": b[i], "index": i} for i in range(n)], key=check)])
    print([(x["index"], x["value"]) for x in sorted([{"value": c[i], "index": i} for i in range(n)], key=check)])
    rez = 0
    arr = [(a, ia), (b, ib), (c, ic)]
    for i in range(3):
        l = arr[0][0]
        il = arr[0][1]
        for j in range(len(arr)):
            if not is_larger(l, arr[j][0], il, arr[j][1]):
                l = arr[j][0]
                il = arr[j][1]
        rez += l[il[-1]]
        rmv = il[-1]
        
        j = 0
        while j < len(arr):
            if l == arr[j][0]:
                del arr[j]
                continue
            arr[j][1].remove(rmv)
            j += 1
    return rez  

t = int(input())
rez = []
while t:
    rez.append(case())
    t -= 1

for r in rez:
    print(r)

'''

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
    ia = [x["index"] for x in sorted([{"value": a[i], "index": i} for i in range(n)], key=check)]
    ib = [x["index"] for x in sorted([{"value": b[i], "index": i} for i in range(n)], key=check)]
    ic = [x["index"] for x in sorted([{"value": c[i], "index": i} for i in range(n)], key=check)]
    print([(x["index"], x["value"]) for x in sorted([{"value": a[i], "index": i} for i in range(n)], key=check)])
    print([(x["index"], x["value"]) for x in sorted([{"value": b[i], "index": i} for i in range(n)], key=check)])
    print([(x["index"], x["value"]) for x in sorted([{"value": c[i], "index": i} for i in range(n)], key=check)])
    rez = 0
    for i in range(3):
        l = a
        il = ia
        if not is_larger(l, b, il, ib):
            l = b
            il = ib
        if not is_larger(l, c, il, ic):
            l = c
            il = ic
        rez += l[il[-1]]
        rmv = il[-1]
        ia.remove(rmv)
        ib.remove(rmv)
        ic.remove(rmv)
        if l == a:
            a = [-1] * len(a)
        if l == b:
            b = [-1] * len(b)
        if l == c:
            c = [-1] * len(c)
    return rez  

'''