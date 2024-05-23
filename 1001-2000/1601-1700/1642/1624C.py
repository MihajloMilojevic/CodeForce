
def case():
    n = int(input())
    a = [int(x) for x in input().split()]
    seen = set()
    for x in a:
        while True:
            if x <= n and x > 0 and x not in seen:
                seen.add(x)
                break
            elif x == 0:
                return "NO"
            x //= 2
    if len(seen) == n:
        return "YES"
    return "NO"

t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)