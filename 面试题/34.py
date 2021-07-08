from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        # 排序后的，建议二分法，先找到target，再确定index
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            elif nums[mid] == target:
                right = mid
        if left < len(nums) and nums[left] == target:
            right = left
            # 向左搜索
            while left >= 0 and nums[left] == target:
                left -= 1
            # 向右搜索
            while right < len(nums) and nums[right] == target:
                right += 1
            return [left+1, right-1]
        else:
            return [-1, -1]


s = Solution()

print(s.searchRange([2,2], 3))

