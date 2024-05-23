n, m = [int(x) for x in input().split(" ")]
donja = n//2+n%2
gornja = n
br = -1
for i in range(donja//m, gornja//m + 1):
    tr = i * m
    if donja <= tr <= gornja:
        br = tr
        break
print(br)