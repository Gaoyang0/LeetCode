from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums) == 0:
        #     return 0
        # nums.sort()
        # max_l = 1
        # cur_l = 1
        # for i in range(1, len(nums)):
        #     if nums[i] - nums[i-1] == 1:
        #         cur_l += 1
        #         max_l = max(max_l, cur_l)
        #     elif nums[i] - nums[i-1] == 0:
        #         continue
        #     else:
        #         cur_l = 1
        # return max_l

        max_l = 0
        num_set = set(nums)
        for num in num_set:
            # num是开头
            if num - 1 not in num_set:
                cur_l = 1
                temp = num
                while temp + 1 in num_set:
                    cur_l += 1
                    temp += 1
                max_l = max(max_l, cur_l)
        return max_l



s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))


