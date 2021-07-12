# 300
from typing import List


# dp[i] = max([dp[j]+1 for j in range(i) if nums[i] > nums[j]])
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(dp)):
            temp = [dp[j]+1 for j in range(i) if nums[i] > nums[j]]
            if temp:
                dp[i] = max(temp)
        return max(dp)



# s = Solution()
# print(s.lengthOfLIS([4,10,4,3,8,9]))

# 1143
# 涉及二维dp了
# dp[i] = dp[j]
class Solution1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]

s1 = Solution1()
print(s1.longestCommonSubsequence("abcde", "ace"))
print(s1.longestCommonSubsequence("bsbininm", "jmjkbkjkv"))