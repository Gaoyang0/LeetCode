from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)

        # 先算前缀
        res[0] = 1
        for i in range(1, len(nums)):
            # 前一个的前缀*前一个数
            res[i] = res[i-1] * nums[i-1]

        # 再算后缀
        temp_r = 1
        for i in range(len(nums)-2, -1, -1):
            temp_r = temp_r * nums[i + 1]
            res[i] = temp_r * res[i]

        return res

s = Solution()

print(s.productExceptSelf([1,2,3,4]))

enumerate