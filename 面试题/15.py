from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 2:
            return []

        res = []
        # 无重复解排序下
        nums.sort()
        for first in range(len(nums)):
            # 因为是三个数，不好考虑，我们默认一次循环把nums[i]选中
            # 剪支
            if nums[first] > 0:
                return res
            if first > 0 and nums[first-1] == nums[first]:
                continue

            left = first + 1
            right = len(nums) - 1

            while left < right:
                if nums[first] + nums[left] + nums[right] == 0:
                    res.append([nums[first], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[first] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return res



s = Solution()
print(s.threeSum([0,0,0]))
print(s.threeSum([-2,0,0,2,2]))