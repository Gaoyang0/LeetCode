from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # s = set()
        # for num in nums:
        #     if num in s:
        #         return num
        #     s.add(num)

        # return -1

        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[i] == nums[nums[i]]:
                return nums[i]
            temp = nums[i]
            nums[i], nums[temp] = nums[temp], nums[i]
        return -1

s = Solution()
print(s.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))