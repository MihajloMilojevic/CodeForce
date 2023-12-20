n = int(input())
x = sorted([int(x) for x in input().split(" ")])
q = int(input())
rez = []
dp = {}
i = n
for c in range(x[-1], -1,-1):
    if c < x[i-1]:
        i = max(0, i-1)
    if c in dp:
        continue
    dp[c] = i

while q:
    q-=1
    m = int(input())
    if m > x[-1]:
        rez.append(n)
    else:
        rez.append(dp[m])

for r in rez:
    print(r)