from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] = nums[i] + nums[i - 1]
        return max(nums)













s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))