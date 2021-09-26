from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
        return dp[-1][-1]

s = Solution()
print(s.maxValue([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))