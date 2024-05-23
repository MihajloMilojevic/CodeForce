string = input()
if len([x for x in string if x == "H" or x == "Q" or x == "9"]) > 0:
    print("YES")
else:
    print("NO")