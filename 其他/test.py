
# class Solution:
#     def fun(self, num):
#         res = []
#         def bak(cur, target):
#             if target == 0:
#                 res.append(cur)
#                 return
#             if target < 0:
#                 return
#             for i in [1, 2, 4]:
#                 if i <= target:
#                     cur.append(i)
#                     bak(cur.copy(), target-i)
#                     cur.pop()
#         bak([], num)
#         return len(res)
#
# s = Solution()
# print(s.fun(4))





