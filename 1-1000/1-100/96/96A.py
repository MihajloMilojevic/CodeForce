sit = input()

max0 = 0
max1 = 0
curr0 = 0
curr1 = 0
for c in sit:
    if c == "0":
        curr0 += 1
        max1 = max(max1, curr1)
        curr1 = 0
    elif c == "1":
        curr1 += 1
        max0 = max(max0, curr0)
        curr0 = 0
max1 = max(max1, curr1)
max0 = max(max0, curr0)
if max0 >= 7 or max1 >= 7:
    print("YES")
else:
    print("NO")