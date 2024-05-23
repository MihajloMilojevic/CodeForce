def hello(s: str):
    i = 0
    for c in "hello":
        ind = s[i:].find(c)
        if ind < 0:
            return False
        i += ind+1
    return True

if hello(input()):
    print("YES")
else:
    print("NO")