# 198
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [nums[0], max(nums[0], nums[1])] + [0] * (len(nums)-2)
        for i in range(2, len(nums)):
            # 只有两个选择, 偷i=>nums[i] + dp[i-2], 不偷i=>dp[i-1]
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[len(nums)-1]