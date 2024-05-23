s, n = [int(x) for x in input().split(" ")]
dragons = []
while n:
    dragons.append([int(x) for x in input().split(" ")])
    n -= 1

dragons.sort(key=lambda x: x[0])
win = True

for d in dragons:
    if s <= d[0]:
        win = False
        break
    s += d[1]

if win:
    print("YES")
else:
    print("NO")