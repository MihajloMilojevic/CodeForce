def case1(inp):
    a, b, x, y, n = [int(x) for x in inp.split()]
    if b < a:
        a, b = b, a
        x, y = y, x
    op = min(n, a-x)
    a -= op
    b -= min(n-op, b-y)
    return a * b
def case2(inp):
    a, b, x, y, n = [int(x) for x in inp.split()]
    if y < x:
        a, b = b, a
        x, y = y, x
    op = min(n, a-x)
    a -= op
    b -= min(n-op, b-y)
    return a * b

def case():
    inp = input()
    return min(case1(inp), case2(inp))

t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())
for r in rez:
    print(r)