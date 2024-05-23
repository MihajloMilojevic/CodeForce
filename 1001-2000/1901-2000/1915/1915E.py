import math

def case():
    n = int(input())
    a = [int(x) for x in input().split()]
    if n == 1:
        return "NO"
    for i in range(n-1):
        if a[i] == a[i+1]:
            return "YES"
    ona = [a[0]]
    onaS = a[0]
    onaI = 2
    on = [a[1]]
    onS = a[1]
    onI = 3
    if onaS == onS:
        return "YES"
    while True:
        # print((onS, onaS), (on, ona))
        if onaS < onS:
            if onaI >= n:
                break
            ona.append(a[onaI])
            onaS += a[onaI]
            onaI += 2
        else:
            if onI >= n:
                break
            on.append(a[onI])
            onS += a[onI]
            onI += 2
        if onaS == onS:
            return "YES"
    ona.reverse()
    on.reverse()
    # print("="*15)
    while len(on) and len(ona):
        # print((onS, onaS), (on, ona))
        if onaS > onS:
            onaS -= ona.pop()
        else:
            onS -= on.pop()
        if onaS == onS:
            return "YES"
    return "NO"

t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)