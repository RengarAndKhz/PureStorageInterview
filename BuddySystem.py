import random


class BuddySystem:
    def __init__(self):
        self.tree = [[0], [0, 0], [0, 0, 0, 1], [0, 1, 1, 0, 0]]

    def setBit(self, offset, length):
        changeStack = []
        for i in xrange(offset, offset+length+1):
            if self.tree[-1][i] == 1:
                continue
            else:
                if changeStack and changeStack[-1]/2 != i/2 or not changeStack:
                    changeStack.append(i)
                self.tree[-1][i] = 1
        for i in xrange(len(self.tree)-2, -1, -1):
            temp = []
            for node in changeStack:
                if node % 2 == 1:
                    if self.tree[i+1][node-1] + self.tree[i+1][node] != 2 and self.tree[i][node/2] != 0:
                        self.tree[i][node/2] = 0
                        if temp and temp[-1]/2 != node/4 or not temp:
                            temp.append(node/2)
                    elif self.tree[i+1][node-1] + self.tree[i+1][node] == 2 and self.tree[i][node/2] == 0:
                        self.tree[i][node/2] = 1
                        if temp and temp[-1] / 2 != node / 4 or not temp:
                            temp.append(node/2)
                else:
                    x = self.tree[i+1][node+1] if node+1 < len(self.tree[i+1]) else 1
                    if self.tree[i+1][node] + x != 2 and self.tree[i][node/2] != 0:
                        self.tree[i][node/2] = 0
                        if temp and temp[-1] / 2 != node / 4 or not temp:
                            temp.append(node/2)
                    elif self.tree[i+1][node] + x == 2 and self.tree[i][node/2] == 0:
                        self.tree[i][node/2] = 1
                        if temp and temp[-1] / 2 != node / 4 or not temp:
                            temp.append(node/2)
            changeStack = temp
        print(self.tree)

    def clearBits(self, offset, length):
        start, end = offset/2, (offset+length)/2
        for i in xrange(offset, offset+length+1):
            self.tree[-1][i] = 0
        for i in xrange(len(self.tree)-2, -1, -1):
            for j in xrange(start, end+1):
                if self.tree[i][j] == 0: continue
                else:
                    if self.tree[i+1][j*2] + (self.tree[i+1][j*2+1] if j*2+1 < len(self.tree[i+1]) else 1) != 2:
                        self.tree[i][j] = 0
            start, end = start/2, end/2
        print(self.tree)

    def setBitsTest(self, offset, length):
        start, end = offset/2, (offset+length)/2
        for i in xrange(offset, offset+length+1):
            self.tree[-1][i] = 1
        for i in xrange(len(self.tree)-2, -1, -1):
            for j in xrange(start, end+1):
                if self.tree[i][j] == 1: continue
                else:
                    if self.tree[i+1][j*2] + (self.tree[i+1][j*2+1] if j*2+1 < len(self.tree[i+1]) else 1) == 2:
                        self.tree[i][j] = 1
            start, end = start/2, end/2
        print(self.tree)





testCase = BuddySystem()
testCase.setBitsTest(1, 3)