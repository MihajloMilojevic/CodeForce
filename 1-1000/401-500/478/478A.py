s = sum([int(x) for x in input().split()])
print(s//5 if s % 5 == 0 and s > 0 else -1)