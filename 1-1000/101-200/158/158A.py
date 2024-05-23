parts = input().split(" ")
n = int(parts[0])
k = int(parts[1]) - 1
a = [int(x) for x in input().split(" ")]
r = 0
for i in range(n):
    if a[i] <= 0 or a[i] < a[k]:
        break
    r += 1

print(r)