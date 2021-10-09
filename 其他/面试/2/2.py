import sys

mat = []
flag = True
for line in sys.stdin:
    if flag:
        flag = False
        mat.append(list(map(int, line.strip()[2:-2].split(","))))
    else:
        mat.append(list(map(int, line.strip()[1:-2].split(","))))
    if line.strip()[-2:] == "]]":
        break

def fun(grid):
    res = 0
    row = len(grid)
    col = len(grid[0])
    def dfs(r, c):
        if 0<=r<row and 0<=c<col and grid[r][c] == 1:
            grid[r][c] = 2
            return 1+dfs(r-1, c) + dfs(r, c-1) + dfs(r+1,c)+dfs(r,c+1)
        return 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                res = max(res, dfs(i, j))

    return res

print(fun(mat))

