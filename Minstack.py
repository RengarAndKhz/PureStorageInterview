class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.flag = False
        self.min = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.flag = True
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x - self.min < 0:
                self.min = x

    def pop(self):
        """
        :rtype: void
        """
        temp  = self.stack.pop()
        if temp < 0:
            self.min -= temp

    def top(self):
        """
        :rtype: int
        """
        temp = self.stack[-1]
        if temp >= 0:
            return self.min + temp
        else:
            return self.min

    def getMin(self):
        """
        :rtype: int
        """
        if self.flag:
            return self.min
        else:
            raise Exception




        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()