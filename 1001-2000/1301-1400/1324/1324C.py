def case():
    s = "R" + input() + "R"
    res = 0
    last = 0
    for i in range(len(s)):
        if s[i] != "R":
            continue
        res = max(res, i - last)
        last = i
    return res

t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)