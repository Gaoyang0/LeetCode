
from typing import List


class Solution:
    def knapsack_problem01(self, w: List[int], v: List[int], max_w: int) -> int:
        '''
        最基本的背包问题就是01背包问题（01 knapsack problem）：
        一共有N件物品，第i（i从1开始）件物品的重量为w[i]，价值为v[i]。
        在总重量不超过背包承载上限W的情况下，能够装入背包的最大价值是多少？
        '''

        # dp[i][j] 表示前 i 件物品体积不超过 j 的情况下能达到的最大价值
        '''
        在我们遍历到第 i 件物品时，在当前背包总容量为 j 的情况下，如果我们不将物品 i 放入背包，
        那么 dp[i][j] = dp[i-1][j]，即前 i 个物品的最大价值等于只取前 i-1 个物品时的最大价值；
        如果我们将物品 i 放入背包，假设第 i 件物品体积为 w，价值为 v，那么我们得到 
        dp[i][j] = dp[i-1][j-w] + v。我们只需在遍历过程中对这两种情况取最大值即可
        '''
        dp = [[0] * (max_w + 1) for _ in range(len(w) + 1)]
        for i in range(1, len(w) + 1):
            for j in range(1, max_w + 1):
                if j >= w[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

    def complete_knapsack_problem(self, w: List[int], v: List[int], max_w: int) -> int:
        '''
        在完全背包问题中，一个物品可以拿多次。
        假设我们遍历到物品 i = 2，且其体积为 w = 2，价值为 v = 3；
        对于背包容量 j = 5，最多只能装下 2 个该物品。那么我们的状态转移方程就变成了
         dp[2][5] = max(dp[1][5], dp[1][3] + 3, dp[1][1] + 6)

        我们发现在 dp[2][3] 的时候我们其实已经考虑了 dp[1][3] 和 dp[2][1]的情况，
        而在时 dp[2][1] 也已经考虑了 dp[1][1] 的情况。因此，对于拿多个物品的情况，
        我们只需考虑 dp[2][3] 即可，即 dp[2][5] = max(dp[1][5], dp[2][3] + 3)。
        这样，我们就得到了完全背包问题的状态转移方程：dp[i][j] = max(dp[i-1][j], dp[i][j-w] + v)，
        其与 0-1 背包问题的差别仅仅是把状态转移方程中的第二个 i-1 变成了 i。
        '''
        dp = [[0] * (max_w + 1) for _ in range(len(w) + 1)]
        for i in range(1, len(w) + 1):
            for j in range(1, max_w + 1):
                if j >= w[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - w[i - 1]] + v[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


s = Solution()
print(s.knapsack_problem01([2, 3, 4, 5], [5, 4, 2, 4], 5))
print(s.complete_knapsack_problem([2, 3, 4, 5], [5, 4, 2, 10], 10))

