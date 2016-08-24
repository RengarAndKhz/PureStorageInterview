class Fibonacci:
    def literator(self, n):
        if n <= 0:
            return 0
        if n in (1, 2):
            return 1
        p1 = 1
        p2 = 1
        for i in xrange(n-2):
            p1, res = p2, p1 + p2
            p2 = res
        return res


    def recursion(self, n):
        if n in (1, 2):
            return 1
        return self.recursion(n-1) + self.recursion(n-2)



testCase = Fibonacci()
print(testCase.recursion(6))