import math

def case():
    n = int(input())
    s = input()
    res = []
    i = 0
    for i in range(n):
        res.append(s[i])
        if i < n - 2 and ((s[i] in "ae" and s[i+2] in "ae") or (s[i] in "bcd" and s[i+1] in "bcd")):
            res.append(".")
    return "".join(res)

t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)