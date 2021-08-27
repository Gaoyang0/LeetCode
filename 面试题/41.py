from typing import List


# 没有出现的最小正整数
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # i = 1
        # s = set(nums)
        # while True:
        #     if i not in s:
        #         return i
        #     i += 1

        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1





s = Solution()
print(s.firstMissingPositive([1,2,0]))
print(s.firstMissingPositive([3,3,-1,1]))
print(s.firstMissingPositive([7,8,9,11,12]))