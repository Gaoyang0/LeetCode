import numpy as np

while True:
    n, m = map(int, input().strip().split(" "))
    res = n
    for i in range(m-1):
        n = np.sqrt(n)
        res += n
    print('%.2f' % res)

