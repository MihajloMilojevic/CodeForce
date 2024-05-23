import math
x, y, z = [int(x) for x in input().split()]
c = int(math.sqrt(z * y / x))
a = z // c
b = y // c
print(4*(a+b+c))