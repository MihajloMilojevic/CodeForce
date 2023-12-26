def dfs(string, seen):
    if string == "":
        return
    if string in seen:
        return
    seen.add(string)
    dfs(string[1:], seen)
    if len(string) > 1:
        dfs(string[0] + string[2:], seen)

def case():
    n = int(input())
    string  = input()
    seen = set()
    dfs(string, seen)
    return len(seen)


t = int(input())
rez = []

while t:
    rez.append(case())
    t -= 1

for r in rez:
    print(r)