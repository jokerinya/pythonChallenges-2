class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    _res = 0
    def divisorSum(self, n):
        self.n = n
        for i in range(1, self.n + 1):
            if self.n % i == 0:
                self._res += i
        return self._res


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)