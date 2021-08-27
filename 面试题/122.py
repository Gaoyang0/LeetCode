from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 表示第i天结束，手里有股票的最大收益
        dp1 = [0] * len(prices)
        # 表示第i天结束，手里没有股票的最大收益
        dp2 = [0] * len(prices)
        dp1[0] = -prices[0]

        for i in range(1, len(prices)):
            # 前一天就有股票，今天购买股票
            dp1[i] = max(dp1[i-1], dp2[i-1] - prices[i])
            # 前一天就没有，今天卖出股票
            dp2[i] = max(dp2[i-1], dp1[i-1] + prices[i])

        return max(max(dp1), max(dp2))


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,1]))