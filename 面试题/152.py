from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 暴力
        # max_product = float("-inf")
        # for i in range(len(nums)):
        #     cur = 1
        #     for j in range(i, len(nums)):
        #         cur *= nums[j]
        #         max_product = max(max_product, cur)
        # return max_product

        # 动态规划
        # res = nums[0]
        # dp_max = [0] * len(nums)
        # dp_min = [0] * len(nums)
        # dp_max[0] = nums[0]
        # dp_min[0] = nums[0]
        #
        # for i in range(1 , len(nums)):
        #     dp_max[i] = max(dp_max[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i])
        #     dp_min[i] = min(dp_max[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i])
        #     res = max(res, dp_max[i])
        # return res

        # 动态规划空间优化
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            # 这里的pre_max, pre_min代表以i为结尾最大，最小子数组的乘积
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res



s = Solution()
print(s.maxProduct([2,3,-2,4]))