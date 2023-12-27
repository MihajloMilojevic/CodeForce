class Till:
    def __init__(self) -> None:
        self.till = {
            25: 0,
            50: 0,
            100: 0
        }
    def add(self, value):
        self.till[value] += 1
        change = value - 25
        n50 = change // 50
        n25= (change % 50) //25
        # print(self.till, n50, n25, change)
        payby25 = self.till[25] >= n25 + 2 * n50
        payby50and25 = self.till[50] >= n50 and self.till[25] >= n25
        # print(payby25, payby50and25)
        if not payby25 and not payby50and25:
            return False
        self.till[25] -= n25
        if self.till[50] < n50:
            self.till[25] -= 2*n25
        else:
            self.till[50] -= n50
        return True
    
def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    till = Till()
    for x in a:
        if not till.add(x):
            return "NO"
    return "YES"
print(solve())