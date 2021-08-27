from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = float("inf")
        res = 0
        for p in prices:
            mi = min(mi, p)
            res = max(res, p-mi)
        return res


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,1]))