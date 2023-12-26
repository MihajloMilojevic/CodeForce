n, t = [int(x) for x in input().split(" ")]
donja = 10**(n-1)
gornja = 10**n - 1
br = -1
for i in range(donja//t, gornja//t + 1):
    tr = i * t
    if donja <= tr <= gornja:
        br = tr
        break
print(br)