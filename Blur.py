
class Blur:
    def __init__(self):
        self.matrix = [[1 for _ in xrange(5)] for _ in xrange(5)]

    def neighbor_blur(self):
        if not self.matrix:
            return
        # from left to right
        for i in xrange(len(self.matrix)):
            p1, p2 = 0, 0
            for j in xrange(len(self.matrix[0])):
                p1, p2, self.matrix[i][j] = p2, self.matrix[i][j], p2 + self.matrix[i][j] + (self.matrix[i][j+1] if j+1 < len(self.matrix[i]) else 0)
        for j in xrange(len(self.matrix[0])):
            p1, p2 = 0, 0
            for i in xrange(len(self.matrix)):
                p1, p2, self.matrix[i][j] = p2, self.matrix[i][j], p2 + self.matrix[i][j] + (self.matrix[i+1][j] if i+1 < len(self.matrix) else 0)
        print(self.matrix)
        for i in xrange(len(self.matrix)):
            for j in xrange(len(self.matrix[0])):
                if (i, j) in ((0, 0), (0, len(self.matrix[0])-1), (len(self.matrix)-1, 0), (len(self.matrix)-1, len(self.matrix[0])-1)):
                    self.matrix[i][j] /= 4
                elif (i == 0 or i == len(self.matrix)-1) or (j == 0 or j == len(self.matrix[0])-1):
                    self.matrix[i][j] /= 6
                else:
                    self.matrix[i][j] /= 9

        print(self.matrix)

testCase = Blur()
testCase.neighbor_blur()