t = int(input())
a = []
while t:
    t -= 1
    a.append(int(input()))

for n in a:
    if n == 1:
        print(1)
        continue
    if n == 2:
        print(-1)
        continue
    num = 1
    for i in range(n):
        for j in range(n):
            print(num, end=" ")
            num += 2
            if num > n**2:
                num = 2
        print()

    