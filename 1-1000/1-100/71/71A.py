def case():
    string = input()
    duz = len(string)
    if duz <= 10:
        return string
    return string[0] + str(duz - 2) + string[-1]



n = int(input())
rez = []
while n:
    rez.append(case())
    n -= 1

for r in rez:
    print(r)