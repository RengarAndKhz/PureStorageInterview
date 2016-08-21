import numpy as np

class BresenhamCircle:
    def __init__(self):
        self.matrix = [[0 for _ in xrange(50)] for _ in xrange(50)]
        self.matrix = np.matrix(self.matrix)
        print(self.matrix)

    def drawCircle(self, a, b, x, y):
        r = 10
        a, b = 25, 25
        x = 0
        y = r
        d = 2 * r + 3
        while x <= y:
            self.drawPoint(a+x, b+y)
            self.drawPoint(a+y, b+x)
            self.drawPoint(a-x, b-y)
            self.drawPoint(a-y, b-y)
            self.drawPoint(a+x, b-y)
            self.drawPoint(a-y, b+x)
            self.drawPoint(a-x, b+y)
            self.drawPoint(a+y, b-x)
            d += 4 * x + 6
            x += 1
            if d > 0:
                d += - 4 * y + 4
                y -= 1



    def drawPoint(self, x, y):
        self.matrix[x][y] = 1


testCase = BresenhamCircle()
