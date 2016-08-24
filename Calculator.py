class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        x = ''
        for item in s:

            if item == " ":
                continue
            elif item.isdigit():
                x += item
            elif item == ")":
                if x:
                    stack.append(x)
                    x = ''
                temp = stack.pop()
                compute = []
                while temp != "(":
                    compute.append(temp)
                    temp = stack.pop()
                stack.append(self.helper(compute))
            else:
                if x:
                    stack.append(x)
                    x = ''
                stack.append(item)
        if x:
            stack.append(x)
        print(stack)

        return self.helper(stack[::-1])

    def helper(self, stack):
        digit = []
        operation = []
        for item in stack:
            if item in ('+', '-'):
                operation.append(item)
            else:
                digit.append(item)
        while operation and len(digit) > 1:

            a = int(digit.pop())
            b = int(digit.pop())

            oper = operation.pop()
            if oper == '+':
                res = a + b
            else:
                res = a - b
            digit.append(str(res))
        return digit[-1]

testCase = Solution()
print(testCase.calculate('(1+(4+5+2)-3)+(6+8)'))

