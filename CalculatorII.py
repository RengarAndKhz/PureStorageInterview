class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = ''
        stack = []
        sign = '+'
        for i in xrange(len(s)):
            if s[i].isdigit():
                num += s[i]
            if (not s[i].isdigit() and s[i] != ' ') or i == len(s)-1:
                if sign == '+':
                    stack.append(int(num))
                if sign == '-':
                    stack.append(-1 * int(num))
                if sign == '*':
                    temp = stack.pop()
                    stack.append(int(temp * float(num)))
                if sign == '/':
                    temp = stack.pop()
                    stack.append(int(temp / float(num)))
                sign = s[i]
                num = ''
        return sum(stack)