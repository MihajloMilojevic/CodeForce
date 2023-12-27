import bisect
cards = [0]
def numH(h):
    if h < len(cards):
        return cards[h]
    num = (h-1)*3+2 + numH(h-1)
    cards.append(num)
    return num

def build(n):
    h = 0
    while numH(h) <= n:
        h += 1
    return h-1

def case():
    n = int(input())
    res = 0
    h = build(n)
    while h:
        n -= cards[h]
        h = build(n)
        res += 1
    return res

t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)