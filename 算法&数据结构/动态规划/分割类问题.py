# 279
# 对于分割类型题,动态规划的状态转移方程通常并不依赖相邻的位置,而是依赖于满足分割条件的位置。
from math import sqrt
# dp数组不断更新覆盖

# 初始化最坏的情况[0, 1, 2, 3, ...]即都是由1相加而成
# 状态转移方程dp[i] = min(dp[i-j**2]+1, dp[i])
# 针对这个状态转移方程需要遍历i(1-n), 内层嵌套j(1-sqrt(n))
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, int(sqrt(i))+1):
                dp[i] = min(dp[i-j**2] + 1, dp[i])
        return dp[n]


# s = Solution()
# print(s.numSquares(12))



from typing import List
# 139
# i=1表示s[0]
# dp[i] = dp[j] && s[j, i] in wordDict (0<=j<i)
class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [True] + [False] * len(s)

        for i in range(1, len(dp)):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[-1]




s1 = Solution1()
print(s1.wordBreak("applepenapple", ["apple", "pen"]))