# class Solution:
#     def singleNumber(self, nums) -> int:
#
#         # 用于保留只出现过一次的数
#         s = set()
#
#         for i in nums:
#             if i not in s:
#                 s.add(i)
#             else:
#                 s.remove(i)
#         return s.pop()
#
#
# s = Solution()
# print(s.singleNumber([2,2,1]))

import typing
print(typing.__file__)