s = input()
sums = [0]
curr = 0
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        curr += 1
    sums.append(curr)
sums.append(curr)
rez = []
m = int(input())
while m:
    m -= 1
    l, r = [int(x) for x in input().split()]
    rez.append(sums[r-1] - sums[l-1])

for r in rez:
    print(r)
