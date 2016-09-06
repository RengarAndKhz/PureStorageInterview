import sys
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        res = []
        right = 0
        left = sys.maxint
        for element in buildings:
            right = max(right, element[1])
            left = min(left, element[0])
        l = [0] * (right - left + 1)
        for element in buildings:
            for i in xrange(element[0], element[1] + 1):
                l[i - left] = max(l[i - left], element[2])
        res.append([left, l[0]])
        for i in xrange(1, len(l)):
            if l[i] > l[i-1]:
                res.append([i+left, l[i]])
            if l[i] < l[i-1]:
                res.append([i-1 + left, l[i]])
        res.append([right, 0])
        return res

testCase = Solution()
print(testCase.getSkyline([ [2,9,10], [3,7,15], [5,12, 12], [15, 20, 10], [19, 24 ,8] ]))