def case():
    s = input()
    for i in range(len(s)-1, -1, -1):
        if s[i] != "0":
            return s[:i]
    return ""
t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)