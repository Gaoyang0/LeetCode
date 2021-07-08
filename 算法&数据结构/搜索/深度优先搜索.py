# 695

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_max = len(grid)
        col_max = len(grid[0])
        # 上左下右
        direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        global_s = set()
        def dfs(row, col):
            s = set()
            stack = [(row, col)]
            while len(stack) > 0:
                temp = stack.pop()
                s.add(temp)
                for d in direct:
                    pos = (temp[0]+d[0], temp[1]+d[1])
                    if 0 <= pos[0] < row_max and 0 <= pos[1] < col_max and grid[pos[0]][pos[1]] == 1 and pos not in s:
                        stack.append(pos)
                        global_s.add(pos)
            return len(s)

        def bfs(row, col):
            s = set()
            q = [(row, col)]
            while len(q) > 0:
                temp = q.pop(0)
                s.add(temp)
                for d in direct:
                    pos = (temp[0] + d[0], temp[1] + d[1])
                    if 0 <= pos[0] < row_max and 0 <= pos[1] < col_max and grid[pos[0]][pos[1]] == 1 and pos not in s:
                        q.append(pos)
                        global_s.add(pos)
            return len(s)

        def dfs_recursion(row, col):
            if 0 <= row < row_max and 0 <= col < col_max and grid[row][col] == 1:
                ans = 1
                # 防止遍历的再遍历
                grid[row][col] = 0
                for d in direct:
                    ans += dfs_recursion(row + d[0], col + d[1])
                return ans
            else:
                return 0

        max_area = 0
        for row in range(row_max):
            for col in range(col_max):
                if grid[row][col] == 1 and (row, col) not in global_s:
                    # temp = dfs(row, col)
                    # temp = bfs(row, col)
                    temp = dfs_recursion(row, col)
                    max_area = max(temp, max_area)
        return max_area


# DFS
s = Solution()
print(s.maxAreaOfIsland([
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]))

# BFS栈实现
# DFS递归版

