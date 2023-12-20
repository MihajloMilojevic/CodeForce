nums = [4, 7,
        44, 47, 74, 77,
        444, 447, 474, 744, 477, 747, 774, 777]

def lucky(n):
    for num in nums:
        if n % num == 0:
            return True
    return False

if lucky(int(input())):
    print("YES")
else:
    print("NO")