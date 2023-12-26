def case():
    n, k = [int(x) for x in input().split()]
    if n % 2 == 0 and k % 2 != 0:
        return "NO"
    if n % 2 != 0 and k % 2 == 0:
        return "NO"
    sumFirstK = (k-1)**2+2*(k-1)+1
    if n < sumFirstK:
        return "NO"
    return "YES"
t = int(input())
rez = []

while t:
    rez.append(case())
    t -= 1

for r in rez:
    print(r)