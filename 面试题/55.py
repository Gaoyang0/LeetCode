from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_l = 0
        for i in range(len(nums)-1):
            if i + nums[i] > max_l:
                max_l = max(max_l, i + nums[i])
                if max_l >= len(nums)-1:
                    return True
        return False


s = Solution()
print(s.canJump([2,3,1,1,4]))