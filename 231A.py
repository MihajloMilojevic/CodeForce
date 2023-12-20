n = int(input())
arr = []
for i in range(n):
    arr.append([int(x) for x in input().split(" ")])
rez = 0
for i in range(n):
    if arr[i][0] + arr[i][1] + arr[i][2] > 1:
        rez += 1
print(rez)