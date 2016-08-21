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
                changeStack.append(i)
                self.tree[-1][i] = 1
        for i in xrange(len(self.tree)-2, -1, -1):
            temp = []
            for node in changeStack:
                if node%2 == 1:
                    if self.tree[i+1][node-1] + self.tree[i+1][node] != 2 and self.tree[i][node/2] != 0:
                        self.tree[i][node/2] = 0
                        temp.append(node/2)
                    elif self.tree[i+1][node-1] + self.tree[i+1][node] == 2 and self.tree[i][node/2] == 0:
                        self.tree[i][node/2] = 1
                        temp.append(node/2)
                else:
                    x = self.tree[i+1][node+1] if node+1 < len(self.tree[i+1]) else 1
                    if self.tree[i+1][node] + x != 2 and self.tree[i][node/2] != 0:
                        self.tree[i][node/2] = 0
                        temp.append(node/2)
                    elif self.tree[i+1][node] + x == 2 and self.tree[i][node/2] == 0:
                        self.tree[i][node/2] = 1
                        temp.append(node/2)
            changeStack = temp
        print(self.tree)















    def clearBit(self, offset, length):
        pass


testCase = BuddySystem()
testCase.setBit(1, 3)