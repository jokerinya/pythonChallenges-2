class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        self.maximumDifference = max(self.__elements)-min(self.__elements)
        print(self.maximumDifference)


a = [1, 2, 5]
d = Difference(a)

d.computeDifference()
