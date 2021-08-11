'''https://zhuanlan.zhihu.com/p/139112162'''

import numpy as np
from math import inf

def Floyd(d):
    n = d.shape[0]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
        print("After %d iteration:\n" % (k+1), d)
    return d


matrix = np.array([[0, 7, inf, inf, 1, 6],
                   [7, 0, 2, 4, inf, inf],
                   [inf, 2, 0, 9, 3, inf],
                   [inf, 4, 9, 0, inf, inf],
                   [1, inf, 3, inf, 0, 3],
                   [6, inf, inf, inf, 3, 0]])

print("Original matrix:\n", matrix)
d_matrix = Floyd(matrix)

# testing
bundle = [[1, 4], [3, 6], [5, 2]]
for i, (start, end) in enumerate(bundle):
    print("Test %d" % (i+1))
    print("The shortest distance between vertex {} and vertex {} is {}".
          format(start, end, int(d_matrix[start-1][end-1])))