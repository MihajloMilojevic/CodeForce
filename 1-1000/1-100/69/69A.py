n = int(input())
v = [0, 0, 0]
while n:
    x,y,z = [int(x) for x in input().split(" ")]
    v[0] += x
    v[1] += y
    v[2] += z
    n-=1

if v[0] == 0 and v[1] == 0 and v[2] == 0:
    print("YES")
else:
    print("NO")