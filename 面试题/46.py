from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 回溯
        res = []
        def back(nums, curr):
            if len(curr) == len(nums):
                res.append(curr)
            elif len(curr) < len(nums):
                candidate = set(nums) - set(curr)
                for i in candidate:
                    temp = curr.copy()
                    temp.append(i)
                    back(nums, temp)
        for i in nums:
            back(nums, [i])
        return res

s = Solution()
print(s.permute([1, 2,4, 3, 5, 6]))