import math

n = int(input())
names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
br = 1
add = 5
while True:
    if n <= add:
        break
    n -= add
    add *= 2
    br *= 2
print(names[(n-1)//(br)])