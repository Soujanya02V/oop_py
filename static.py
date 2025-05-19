class math:
    def __init__(self, num):
        self.num = num

    def addto(self, n):
        self.num = self.num + n
    @staticmethod
    def add(a,b):
        return a+b
result = math.add(1,2)
print(result)
a = math(5)
print(a.num)
a.addto(6)
print(a.num)
