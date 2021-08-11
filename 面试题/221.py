from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 思考: 重叠子问题，最优子结构，状态转移方程

        '''
        dp[i][j] 表示以(i,j) 为右下角，且只包含 1 的正方形的边长最大值。
        dp[i][j]=min(dp[i][j−1],dp[i−1][j],dp[i−1][j−1])+1

        假设min(dp[i][j−1],dp[i−1][j],dp[i−1][j−1]) = a
        那么有dp[i][j−1] >= a and dp[i−1][j] >= a and dp[i−1][j−1] >= a
        如果在图上看的话就可以保证斜对角为[i-a][j-a] -- [i][j]除了[i][j]全是1
        那么如果[i][j]是1的话dp[i][j]=a+1
        '''
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide * maxSide
        return maxSquare



s = Solution()
print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))