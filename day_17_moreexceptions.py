class Calculator():
    def power(self, n, p):
        self.n, self.p = n, p
        return (self.n ** self.p) if (self.n >= 0 and self.p >= 0) else "n and p should be non-negative"

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e) 