rez = {0: 0}


t = int(input())
a = []
while t:
    a.append(int(input()))
    t -= 1

for i in range(1, max(a)//2+1):
    rez[i] = rez[i-1] + 8 * i * i

for x in a:
    print(rez[x//2])
