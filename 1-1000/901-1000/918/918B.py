for i in range(1, 11):
    res = 0
    l = []
    for j in range(10**(i-1), 10**i):
        if sum([int(x) for x in list(str(j))]) == 10:
            res += 1
    print(i, res)
    l.append(res)