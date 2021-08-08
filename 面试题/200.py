from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        row_max = len(grid)
        col_max = len(grid[0])
        # 上左下右
        direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def dfs(row, col):
            stack = [(row, col)]
            while len(stack) > 0:
                temp = stack.pop()
                grid[temp[0]][temp[1]] = '2'
                for d in direct:
                    pos = (temp[0] + d[0], temp[1] + d[1])
                    if 0 <= pos[0] < row_max and 0 <= pos[1] < col_max and grid[pos[0]][pos[1]] == '1':
                        stack.append(pos)

        # def bfs(row, col):
        #     q = [(row, col)]
        #     while len(q) > 0:
        #         temp = q.pop(0)
        #         grid[temp[0]][temp[1]] = '2'
        #         for d in direct:
        #             pos = (temp[0] + d[0], temp[1] + d[1])
        #             if 0 <= pos[0] < row_max and 0 <= pos[1] < col_max and grid[pos[0]][pos[1]] == '1':
        #                 q.append(pos)

        res = 0
        for row in range(row_max):
            for col in range(col_max):
                if grid[row][col] == "1":
                    dfs(row, col)
                    # bfs(row, col)
                    res += 1
        return res


s = Solution()
print(s.numIslands([["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]
))