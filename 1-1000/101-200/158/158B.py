import math

n = int(input())
g = [int(x) for x in input().split(" ")]
obj = {
    1: 0,
    2: 0,
    3: 0,
    4: 0
}
for x in g:
    obj[x]+=1
rez = obj[4]

# grupisemo 3 i 1
g = min(obj[1], obj[3])
rez += obj[3]
obj[1] -= g

# grupisemo 2 i 2
g = obj[2] // 2
rez += g
obj[2] -= g * 2

if obj[2] == 1:
    rez += 1
    obj[1] -= min(obj[1], 2)

rez += math.ceil(obj[1]/4)

print(rez)