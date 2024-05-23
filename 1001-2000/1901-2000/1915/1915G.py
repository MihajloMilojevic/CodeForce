import math

def case():
    n, m = [int(x) for x in input().split()]
    edges = {i: list() for i in range(n)}
    print(edges)
    dp = [-1] * n
    seen = set()
    bikes = []
    for i in range(m):   
        u, v, w = [int(x) for x in input().split()]
        edges[u-1].append((v-1, w))
        edges[v-1].append((u-1, w))
    print(edges)
    s = [int(x) for x in input().split()]
    def dfs(source):
        if len(bikes) == 0:
            bikes.append(s[source])
        else:
            bikes.append(min(s[source], bikes[-1]))
        print(source)
        if source == n - 1:
            return 0
        if source in seen:
            return dp[source]
        seen.add(source)
        res = -1
        for next, w in edges[source]:
            if next in seen:
                continue
            x = dfs(next)
            if x < 0:
                continue
            x += bikes[-1]*w
            if res == -1:
                res = x
            else:
                res = min(x, res)
        print(f"SOURCE: {source}, RES: {res}")
        dp[source] = res
        bikes.pop()
        return res
    return dfs(0)
t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)