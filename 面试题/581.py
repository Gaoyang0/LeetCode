from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 分析
        # 左边是升序，右边是升序，右边最小大于左边最大
        # 中间最小大于左边最大，中间最大小于右边最小
        l, r = 0, len(nums)-1
        while l+1 < len(nums) and nums[l+1] >= nums[l]:
            l += 1
        while r-1 >= 0 and nums[r-1] <= nums[r]:
            r -= 1
        if l == len(nums) - 1 and r == 0:
            return 0

        mid_max = max(nums[l+1:r],default=nums[r]+1)
        mid_min = min(nums[l+1:r],default=nums[l]-1)

        flag = True
        while flag:
            flag = False
            if r < len(nums) and mid_max > nums[r]:
                r += 1
                flag = True
            if l >= 0 and mid_min < nums[l]:
                l -= 1
                flag = True
            mid_max = max(nums[l+1:r])
            mid_min = min(nums[l+1:r])
        return r-l-1

        # if (l+1 == r and nums[l] < nums[r]) or (l==0 and r==len(nums)-1):
        #     return len(nums)
        # mid_max = max(nums[l:r])
        # mid_min = min(nums[l:r])
        # flag = True
        # while flag:
        #     flag = False
        #     if r < len(nums) and mid_max > nums[r]:
        #         r += 1
        #         flag = True
        #     if l-1 >= 0 and mid_min < nums[l]:
        #         l -= 1
        #         flag = True
        #     mid_max = max(nums[l:r])
        #     mid_min = min(nums[l:r])
        # return r-l if temp_l == l or temp_r == r else r-l-1



s = Solution()
print(s.findUnsortedSubarray(
    [2,1]))