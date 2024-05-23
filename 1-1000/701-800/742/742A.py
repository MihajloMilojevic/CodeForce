n = int(input())
rem = n % 4
if n == 0:
    print(1)
elif rem == 1:
    print(8)
elif rem == 2:
    print(4)
elif rem == 3:
    print(2)
else:
    print(6)