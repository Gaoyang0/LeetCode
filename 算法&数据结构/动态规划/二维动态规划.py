from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row_max = len(grid)
        col_max = len(grid[0])

        # 初始化辅助数组
        dp = [[0 for _ in range(col_max)] for _ in range(row_max)]
        dp[0][0] = grid[0][0]

        for r in range(row_max):
            for c in range(col_max):
                if r == 0 and c == 0:
                    continue
                elif r == 0:
                    dp[r][c] = dp[r][c-1] + grid[r][c]
                elif c == 0:
                    dp[r][c] = dp[r-1][c] + grid[r][c]
                else:
                    dp[r][c] = min(dp[r][c-1], dp[r-1][c]) + grid[r][c]

        return dp[row_max-1][col_max-1]


s = Solution()
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))