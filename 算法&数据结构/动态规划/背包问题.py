
from typing import List


class Solution:
    def knapsack_problem01(self, w: List[int], v: List[int], max_w: int) -> int:
        '''
        最基本的背包问题就是01背包问题（01 knapsack problem）：
        一共有N件物品，第i（i从1开始）件物品的重量为w[i]，价值为v[i]。
        在总重量不超过背包承载上限W的情况下，能够装入背包的最大价值是多少？
        dp[i][j]表示将前i件物品装进限重为j的背包可以获得的最大价值, 0<=i<=N, 0<=j<=W
        当i>0时，dp[i][j]有两种情况
        1. 不转装入第i个物品，则dp[i][j] <- dp[i-1][j]
        2. 装入第i个物品(在能装入的前提下)，则dp[i][j] = dp[i-1][j-w[i]] + v[i]
        其中，dp[i][j]由dp[i-1][0~j]决定，可以去掉dp的一维来简化
        '''
        dp = [[0] * (max_w+1) for _ in range(len(w)+1)]
        # 遍历i
        for i in range(1, len(w)+1):
            for j in range(1, max_w+1):
                if j < w[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])
        return dp[-1][-1]

    def unbounded_knapsack_problem(self, w: List[int], v: List[int], max_w: int) -> int:
        '''
        完全背包（unbounded knapsack problem）与01背包不同就是每种物品可以有无限多个：
        一共有N种物品，每种物品有无限多个，第i（i从1开始）种物品的重量为w[i]，价值为v[i]。
        '''

        pass


s = Solution()
print(s.knapsack_problem01([2, 3, 4, 5], [3, 1, 1, 4], 8))












#
# # 416
# from typing import List
#
#
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         s = sum(nums)
#         if s % 2 == 0:
#             target = s // 2
#             set = set(nums)
#
#         else:
#             return False
#
#
#
# s = Solution()
# print(s.canPartition([1, 5, 11, 5]))
# print(s.canPartition([1, 2, 3, 5]))
