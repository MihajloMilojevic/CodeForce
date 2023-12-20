n = int(input())
x = 0
while n:
    op = input()
    if "++" in op:
        x += 1
    else:
        x -= 1 
    n -= 1

print(x)