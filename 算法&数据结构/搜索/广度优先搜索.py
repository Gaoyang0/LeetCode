# 934
from typing import List
import copy
import queue

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        # 1. DFS找到第一个岛屿
        # 2. 从第一个岛屿的边缘出发，使用BFS找到第二个岛屿(BFS的层数即为最短路程)

        row_max = len(grid)
        col_max = len(grid[0])
        direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def get_first_land():
            for row in range(row_max):
                for col in range(col_max):
                    if grid[row][col] == 1:
                        return row, col

        def DFS(row, col):
            margin_set = set()
            stack = [(row, col)]
            while len(stack) > 0:
                temp = stack.pop()
                # 标记为2,方便DFS不再遍历,也方便BFS区分
                grid[temp[0]][temp[1]] = 2
                for d in direct:
                    pos = (d[0]+temp[0], d[1]+temp[1])
                    if 0 <= pos[0] < row_max and 0 <= pos[1] < col_max:
                        if grid[pos[0]][pos[1]] == 0:
                            margin_set.add(temp)
                        elif grid[pos[0]][pos[1]] == 1:
                            stack.append(pos)
            return margin_set

        def BFS(row, col):
            grid_copy = copy.deepcopy(grid)
            q = queue.Queue()
            q.put((row, col, 0))
            while not q.empty():
                r, c, layer = q.get()
                if grid_copy[r][c] == 1:
                    return layer
                grid_copy[r][c] = 3
                for d in direct:
                    pos = (r+d[0], c+d[1])
                    if 0 <= pos[0] < row_max and 0 <= pos[1] < col_max and \
                            (grid_copy[pos[0]][pos[1]] == 1 or grid_copy[pos[0]][pos[1]] == 0):
                            q.put((pos[0], pos[1], layer+1))
            return row_max + col_max

        row, col = get_first_land()
        margin_set = DFS(row, col)

        # 解法一
        # min_len = row_max + col_max
        # for row, col in margin_set:
        #     length = BFS(row, col)
        #     min_len = min(length-1, min_len)
        # return min_len

        q = list(margin_set)
        step = 0
        while len(q) > 0:
            l = len(q)
            # 一次while循环检测所有同一层的点
            for _ in range(l):
                r, c = q.pop(0)
                for d in direct:
                    pos = (r + d[0], c + d[1])
                    if 0 <= pos[0] < row_max and 0 <= pos[1] < col_max:
                        if grid[pos[0]][pos[1]] == 0:
                            q.append(pos)
                        elif grid[pos[0]][pos[1]] == 1:
                            return step
                        grid[pos[0]][pos[1]] = 2
            step += 1






s = Solution()
# print(s.shortestBridge([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],[0,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0],[1,1,1,1,1,0,1,1,0,1,0,1,1,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1,1,0,1,1,1,0,0,0,0,0,0],[0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],[0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],[0,0,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0]]))
# print(s.shortestBridge( [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))
# print(s.shortestBridge([[0,1,0,0,0],[0,1,0,1,1],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0]]))
print(s.shortestBridge([[0,0,0,1,1],[0,0,0,1,0],[0,0,0,1,1],[0,0,1,0,1],[0,0,1,1,0]]))