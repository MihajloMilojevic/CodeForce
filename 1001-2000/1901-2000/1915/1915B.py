def case():
    sq = [input(), input(), input()]
    for r in sq:
        if "?" in r:
            if "A" not in r:
                return "A"
            if "B" not in r:
                return "B"
            if "C" not in r:
                return "C"
    return ""

t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)