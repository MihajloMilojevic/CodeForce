parts = input().split(" ")
n = int(parts[0])
k = int(parts[1])-1
pola = (n+1)//2
rez = 0
if k < pola:
    rez = k * 2 + 1
else:
    rez = (k-pola)*2 + 2
print(rez)