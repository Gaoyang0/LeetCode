from typing import List
from collections import Counter



class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 暴力
        # res = 0
        # for l in range(len(nums)):
        #     for r in range(l, len(nums)):
        #         if sum(nums[l:r+1]) == k:
        #             res += 1
        # return res

        # 优化
        # dic = Counter({0: 1})
        # res = pre_sum = 0
        # for i in nums:
        #     pre_sum += i
        #     res += dic[pre_sum - k]
        #     dic[pre_sum] += 1
        # return res

        pre_sum = 0
        res = 0
        count = {}
        for num in nums:
            pre_sum += num
            if pre_sum == k:
                res += 1
            if pre_sum - k in count:
                res += count[pre_sum - k]
            count[pre_sum] = count.get(pre_sum, 0) + 1
        return res




s = Solution()
print(s.subarraySum([1,1,1], 2))