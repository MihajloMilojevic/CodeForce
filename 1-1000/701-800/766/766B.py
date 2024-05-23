def check(a, b, c):
    return a + b > c and a + c > b and b + c > a

n = int(input())
a = sorted([int(x) for x in input().split()])
l = n - 3
while l >= 0:
    if check(a[l], a[l+1], a[l+2]):
        print("YES")
        exit()
    l -= 1
print("NO")