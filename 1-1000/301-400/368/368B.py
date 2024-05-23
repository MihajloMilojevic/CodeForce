n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
dp = [0] * n
s = set()
for i in range(n-1, -1, -1):
    s.add(a[i])
    dp[i] = len(s)

rez = []
while m:
    m -=1
    rez.append(dp[int(input())-1])


for r in rez:
    print(r)