from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 动态规划：最优子结构，重叠子问题，状态转移方程
        # dp[i] = min([dp[i-j] for j in coins])

        # dp = [float("inf")] * (amount + 1)
        # dp[0] = 0
        #
        # for coin in coins:
        #     for i in range(coin, amount + 1):
        #         dp[i] = min(dp[i], dp[i - coin] + 1)
        #
        # return dp[-1] if dp[-1] != float("inf") else -1

        # dp[i]代表amount为i的时候最小硬币数
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount+1):
            # 试一下所有的硬币
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[-1] if dp[-1] != float("inf") else -1


s = Solution()
print(s.coinChange([1, 2, 5], 11))