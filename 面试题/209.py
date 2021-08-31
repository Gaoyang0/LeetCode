from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 1
        s = nums[0]
        res = []
        while l < r <= len(nums):
            if s >= target:
                if r - l == 1:
                    return 1
                else:
                    res.append(r-l)
                    s -= nums[l]
                    l += 1
            else:
                if r < len(nums):
                    s += nums[r]
                r += 1
        return 0 if len(res) == 0 else min(res)


s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
print(s.minSubArrayLen(1, [2,3,1,2,4,3]))
print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))