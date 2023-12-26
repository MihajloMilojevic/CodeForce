def case():
    A, B = [int(x) for x in input().split()]
    if A == B:
        return "NO"
    t = 1
    while True:
        t += 1
        X = A * B
        Y = t * A
        Z = (B + t) * A
        distinct = X != Y and X != Z and Y != Z
        xisGood = X % A == 0 and X % B == 0
        yisNearly = Y % A == 0 and Y % B != 0
        zisNearly = Z % A == 0 and Z % B != 0
        if distinct and xisGood and yisNearly and zisNearly:
            break
    return f"YES\n{X} {Y} {Z}"

t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())
for r in rez:
    print(r)