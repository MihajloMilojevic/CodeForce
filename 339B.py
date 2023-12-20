n, m = [int(x) for x in input().split(" ")]
a = [int(x) for x in input().split(" ")]
t = a[0]-1
for i in range(m-1):
    t += (a[i+1]-a[i]+n)%n

print(t)