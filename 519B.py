def createMap(x):
    mapX = {}
    for y in x:
        if y not in mapX:
            mapX[y] = 0
        mapX[y]+=1
    return mapX
def diff(mapX, mapY):
    for key in mapX:
        if key not in mapY:
            return key
        if mapX[key] != mapY[key]:
            return key
    return -1
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
mapA = createMap(a)
mapB = createMap(b)
mapC = createMap(c)
print(diff(mapA, mapB))
print(diff(mapB, mapC))