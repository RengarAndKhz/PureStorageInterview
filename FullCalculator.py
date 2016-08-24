class Solution:
    def calculator(self, s):
        num = ''
        stack = []
        for item in s:
            if item == ' ': continue
            if item.isdigit():
                num += item
            elif item in '(+-*/':
                if num:
                    stack.append(int(num))
                    num = ''
                stack.append(item)
            elif item == ')':
                if num:
                    stack.append(int(num))
                    num = ''
                x = stack.pop()
                temp = []
                while x != '(':
                    temp.append(x)
                    x = stack.pop()
                stack.append(self.helper(temp[::-1]))
        if num:
            stack.append(int(num))
        return self.helper(stack)


    def helper(self, stack):
        sign = '+'
        compute = []
        for item in stack:
            if isinstance(item, int):
                if sign == '+':
                    compute.append(item)
                elif sign == '-':
                    compute.append(-1 * item)
                elif sign == '*':
                    x = compute.pop()
                    compute.append(x * item)
                else:
                    x = compute.pop()
                    compute.append(int(x / float(item)))
            else:
                sign = item
        return sum(compute)


testCase = Solution()
print(testCase.calculator('(2 + 3) * (3 + 2)'))