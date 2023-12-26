n, m = [int(x) for x in input().split()]
translation = {}
for i in range(m):
    a, b = input().split()
    if len(a) <= len(b):
        translation[a] = a
    else:
        translation[a] = b

text = [translation[word] for word in input().split()]
print(" ".join(text))