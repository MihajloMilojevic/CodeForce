def case():
    n = int(input())
    stringSet = set()
    stringList = list()
    for _ in range(n):
       x = input()
       stringSet.add(x)
       stringList.append(x)
    rez = []
    for s in stringList:
        found = False
        for i in range(1, len(s)):
            l = s[:i]
            r = s[i:]
            if l in stringSet and r in stringSet:
                found = True
                break
        rez.append("1" if found else "0")
    return "".join(rez)

t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)