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
        # y = (sum(nums) - target) // 2
        # (sum(nums) - target) // 2 ==>是已知的，答案等价于的y的所有可能数

        s = sum(nums)
        if (s - target) % 2 != 0:
            return 0
        target = (s - target) // 2

        # 01背包问题







s = Solution()
print(s.findTargetSumWays(
[27,33,4,43,31,44,47,6,6,11,39,37,15,16,8,19,48,17,18,39], 24))