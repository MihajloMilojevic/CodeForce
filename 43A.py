n = int(input())

count = {}
while n:
    n -= 1
    x = input()
    if x not in count:
        count[x] = 0
    count[x] += 1
    
res = list(count.keys())[0]
for key in count:
    if count[key] > count[res]:
        res = key

print(res)