class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for item in tokens:
            if item.isdigit() or item[1:].isdigit():
                stack.append(int(item))
            else:
                b = stack.pop()
                a = stack.pop()

                if item == '+':
                    temp = a + b
                elif item == '-':
                    temp = a - b
                elif item == '*':
                    temp = a * b
                else:
                    temp = a / b
                print(temp)
                stack.append(temp)
        return stack[-1]

testCase = Solution()
print(testCase.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

