def blur(matrix):
    for i in xrange(len(matrix)):
        pre = 0
        for j in xrange(len(matrix[0])):
            temp = matrix[i][j]
            matrix[i][j] += pre + (matrix[i][j+1] if j+1 < len(matrix[0]) else 0)
            pre = temp
    for j in xrange(len(matrix[0])):
        pre = 0
        for i in xrange(len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] += pre + (matrix[i+1][j] if i+1 < len(matrix) else 0)
            pre = temp
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[0])):
            if (i, j) in {(0, 0), (0, len(matrix[0])-1), (len(matrix)-1, 0), (len(matrix)-1, len(matrix[0])-1)}:
                matrix[i][j] /= 4
            elif (i == 0 or i == len(matrix)-1) or (j == 0 or j == len(matrix[0])-1):
                matrix[i][j] /= 6
            else:
                matrix[i][j] /= 9
matrix = [[1 for _ in xrange(5)] for _ in xrange(5)]
blur(matrix)
print(matrix)