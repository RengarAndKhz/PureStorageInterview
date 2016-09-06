import numpy as np
l = []
def circle(matrix, x, y, r):
    value = 10
    i = 0
    j = r
    d = -2 * r + 3
    while i <= j:
        draw(matrix, x + i, y + j, value)
        draw(matrix, x + j, y + i, value)
        draw(matrix, x + i, y - j, value)
        draw(matrix, x - j, y + i, value)
        draw(matrix, x - i, y + j, value)
        draw(matrix, x + j, y - i, value)
        draw(matrix, x - i, y - j, value)
        draw(matrix, x - j, y - i, value)
        if d < 0:
            d += 4 * i + 6
            i += 1
        else:
            d += 4 * i + 6 - 4*j+ 4
            i += 1
            j -= 1

def draw(matrix, x, y, value):
   l.append((x, y))


matrix = [[0 for _ in xrange(10)] for _ in xrange(10)]
circle(matrix, 5, 5, 1)
for x, y in l:
    matrix[len(matrix)-1-y][x] = 1
matrix = np.matrix(matrix)
print(matrix)