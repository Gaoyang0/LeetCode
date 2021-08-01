
from typing import List


class Solution:
    def knapsack_problem01(self, w: List[int], v: List[int], max_w: int) -> int:
        '''
        最基本的背包问题就是01背包问题（01 knapsack problem）：
        一共有N件物品，第i（i从1开始）件物品的重量为w[i]，价值为v[i]。
        在总重量不超过背包承载上限W的情况下，能够装入背包的最大价值是多少？
        '''
        dp = [[0] * (max_w + 1) for _ in range(len(w) + 1)]
        for i in range(1, len(w) + 1):
            for j in range(1, max_w + 1):
                if j > w[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]

class Solution:
    def knapsack_problem(self, w: List[int], v: List[int], max_w: int) -> int:
        pass


s = Solution()
print(s.knapsack_problem([2, 3, 4, 5], []))













# 416
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 0:
            target = s // 2
            set = set(nums)

        else:
            return False



s = Solution()
print(s.canPartition([1, 5, 11, 5]))
print(s.canPartition([1, 2, 3, 5]))
