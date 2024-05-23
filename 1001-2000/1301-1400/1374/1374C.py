def case():
    n = input()
    s = input()
    res = 0
    stk = 0
    for c in s:
        if c == "(":
            stk += 1
        else:
            stk -= 1
        if stk < 0:
            res += 1
            stk = 0
    return res


t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)