import math

n, m, a = [int(x) for x in input().split(" ")]
w = math.ceil(n/a)
h = math.ceil(m/a)
print(w*h)