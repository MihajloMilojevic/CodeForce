n = int(input())
rez = 0
for i in range(1, n+1):
    rez += (n-i)*i + 1

print(rez)