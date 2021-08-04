from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 回溯超时
        # 时间复杂度时间复杂度：O(2^n)
        # def back(index, cur):
        #     if index == len(nums) - 1 and cur == target:
        #         self.res += 1
        #     if index + 1 < len(nums):
        #         back(index+1, cur+nums[index+1])
        #         back(index+1, cur-nums[index+1])
        #
        # back(0, nums[0])
        # back(0, -nums[0])
        # return self.res

        # 动态规划
        # 设 + 部分数组和为：x， - 部分数字和为：y，可以推出
        # x - y = target
        # x + y = sum(nums)
        # x = (sum(nums) - target) // 2
        # (sum(nums) - target) // 2 ==>是已知的，答案等价于的y的所有可能数

        s = sum(nums)
        if (s - target) % 2 != 0 or s < target:
            return 0
        target = (s - target) // 2

        # 01背包问题
        max_w = target
        dp = [[0] * (max_w + 1) for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(max_w + 1):
                if j < nums[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]

        return dp[-1][-1]







s = Solution()
print(s.findTargetSumWays(

[2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53], 1000))