def case():
    n = int(input())
    string = input()
    niz = [0]*26
    br = 0
    for char in string:
        c = ord(char) - ord("A")
        if niz[c] < 0:
            continue
        niz[c] += 1
        if niz[c] >= c + 1:
            br += 1
            niz[c] = -1
    return br






t = int(input())
rez = []
while t:
    rez.append(case())
    t -= 1

for r in rez:
    print(r)
