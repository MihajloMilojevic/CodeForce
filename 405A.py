n = int(input())
a = [int(x) for x in input().split(" ")]
so = sorted(a)
h = so[-1]
rot = []
trH = 0
for i in range(h):
    while trH < len(so) and so[trH] <= i + 1:
        trH += 1
    rot.append(trH)

so = sorted(rot)
h = so[-1]
rot = []
trH = 0
for i in range(h):
    while trH < len(so) and so[trH] < i + 1:
        trH += 1
    rot.append(trH+1)
print(" ".join([str(x) for x in rot]))