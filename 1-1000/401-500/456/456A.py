n = int(input())
laptops = []
while n:
    n -= 1
    a, b = [int(x) for x in input().split()]
    laptops.append((a, b))

laptops.sort(key=lambda x: x[1])
happy = False
for i in range(len(laptops)-1):
    if laptops[i][0] > laptops[i+1][0]:
        happy = True
        break

if happy:
    print("Happy Alex")
else:
    print("Poor Alex")