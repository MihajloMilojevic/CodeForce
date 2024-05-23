def f(a,x):
    return x //a + x % a


def case():
    p = input().split(" ")
    l = int(p[0])
    r = int(p[1])
    a = int(p[2])
    m = f(a, r)
    can = r - r%a -1
    if can >= l:
        m = max(m, f(a, can))
    return m


t = int(input())
rez = []
while t:
    rez.append(case())
    t -= 1

for r in rez:
    print(r)