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
x = min(g[1], g[3])
g[1] -= x
rez += g[3]

if(g[1] <= g[2]):
    g[1] = 0

# g13 = min(obj[1], obj[3])
# obj[1] -= g13
# obj[3] -= g13

# g12 = min(obj[1], obj[2])
# obj[1] -=  g12
# obj[2] -= g12

# g22 = obj[2]//2
# obj[2] -= g22 * 2

# g114 = obj[1] //4
# obj[1] -= g114 * 4

# g113 = obj[1] //3
# obj[1] -= g113 * 3

# g112 = obj[1] //2
# obj[1] -= g112 * 2


# print(obj[1] + obj[2] + obj[3] + obj[4] + g13 + g12 + g22 + g114 + g113 + g112)