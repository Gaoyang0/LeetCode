# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         dp = [[False] * n for _ in range(n)]
#
#         start = 0
#         max_len = 0
#
#
#         if n < 2:
#             return s
#
#         for i in range(n):
#             dp[i][i] = True
#
#         # 边界, i+1:j-1 and s[i]==s[j]
#         for j in range(1, n):
#             for i in range(j):
#                 # 长度为2
#                 if j - i == 1:
#                     dp[i][j] = True if s[i] == s[j] else False
#                 else:
#                     dp[i][j] = dp[i+1][j-1] and (True if s[i] == s[j] else False)
#
#                 if dp[i][j] and j-i+1 > max_len:
#                     start = i
#                     max_len = j-i+1
#         return s[start:start+max_len]
#
#
# s = Solution()
# print(s.longestPalindrome("ada"))

#
# class Solution:
#     def maxArea(self, height):
#
#         max_water = 0
#
#         # 暴力解法
#         # for i in range(len(height) - 1):
#         #     for j in range(i + 1, len(height)):
#         #         water = (j - i) * min(height[i], height[j])
#         #         if water > max_water:
#         #             max_water = water
#         #             print(j-i, min(height[i], height[j]))
#         #
#         # return max_water
#
#         # 双指针
#         i, j = 0, len(height)-1
#
#         while i < j:
#             water = (j-i)*min(height[i], height[j])
#             if max_water < water:
#                 max_water = water
#             if height[i] < height[j]:
#                 temp = height[i]
#                 while height[i] <= temp and i < j:
#                     i += 1
#             else:
#                 temp = height[j]
#                 while height[j] <= temp and j > i:
#                     j -= 1
#         return max_water
#
# s = Solution()
# print(s.maxArea([1,8,6,2,5,4,8,3,7]))


class Solution:
    def threeSum(self, nums):
        n = len(nums)
        res = []
        # 特殊情况
        if not nums or n < 3:
            return []
        nums.sort()

        for i in range(n):
            # nums[i] > 0表示右侧不会有解了
            if nums[i] > 0:
                return res

            # 跳过重复元素，避免重复解
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 双指针
            L = i + 1
            R = n - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    # 新解
                    res.append([nums[i], nums[L], nums[R]])
                    # 避免重复解
                    while (L < R and nums[L] == nums[L + 1]):
                        L += 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R -= 1
                    L += 1
                    R -= 1
                elif nums[i] + nums[L] + nums[R] < 0:
                    L += 1
                else:
                    R -= 1

        return res

s = Solution()

print(s.threeSum([-1,0,1,2,-1,-4]))