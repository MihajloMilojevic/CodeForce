def case():
    s = input()
    if "1" not in s or "0" not in s:
        return s
    if s[0] == "1":
        p = "10"
    else:
        p = "01"
    return p * len(s)
t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)