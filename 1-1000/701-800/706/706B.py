n = int(input())
x = sorted([int(x) for x in input().split(" ")])
q = int(input())
rez = []
dp = {}
ind = 0
for i in range(x[-1]+1):
    if ind >= n:
        dp[i] = n
        continue
    if x[ind] == i:
        k = x[ind]
        while  ind < n and k == x[ind]:
            ind += 1
    dp[i] = ind
# print(dp)
while q:
    q-=1
    m = int(input())
    if m >= x[-1]:
        rez.append(n)
    else:
        rez.append(dp[m])

for r in rez:
    print(r)