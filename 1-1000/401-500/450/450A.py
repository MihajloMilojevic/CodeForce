n, m = [int(x) for x in input().split()]
a = [0] + [int(x) for x in input().split()]
b = [0] * (n+1)
last = 1
end = False
while not end:
    end = True
    for i in range(1, n+1):
        if b[i] < 0:
            continue
        end = False
        b[i] += m
        if b[i] >= a[i]:
            b[i] = -1
            last = i

print(last)