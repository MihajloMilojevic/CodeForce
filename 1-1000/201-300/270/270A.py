

t = int(input())
rez = []

while t:
    t-=1
    a = int(input())
    if 360 % (180-a) == 0:
        rez.append("YES")
    else:
        rez.append("NO")

for r in rez:
    print(r)