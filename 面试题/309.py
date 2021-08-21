from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        # f[i][0]: 手上持有股票的最大收益
        # f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
        # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
        f = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
        for i in range(1, n):
            # 前一天持有的，当天买入的
            f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
            # 当天买
            f[i][1] = f[i - 1][0] + prices[i]
            # 前一天就不持有且处于冷冻期，前一天不持有且处于不冷冻期
            f[i][2] = max(f[i - 1][1], f[i - 1][2])

        return max(f[n - 1][1], f[n - 1][2])



s = Solution()
print(s.maxProfit([1,2,3,0,2]))