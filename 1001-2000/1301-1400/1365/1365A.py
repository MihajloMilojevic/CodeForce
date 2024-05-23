nameA = "Ashish"
nameV = "Vivek"
def case():
    n, m = [int(x) for x in input().split()]
    numR = 0
    numC = 0
    cols = [True] * m
    for i in range(n):
        row = input()
        if "1" not in row:
            numR += 1
        row = row.split()
        for j in range(m):
            if row[j] == "1":
                cols[j] = False
    numC = cols.count(True)
    return nameA if min(numR, numC) %2 != 0 else nameV

t = int(input())
rez = []
while t:
    t -= 1
    rez.append(case())

for r in rez:
    print(r)