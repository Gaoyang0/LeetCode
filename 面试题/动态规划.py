class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        start = 0
        max_len = 1

        # 特殊情况
        if n < 2:
            return s

        # 初始化dp表
        for i in range(n):
            dp[i][i] = True

        # 长度为2, dp[i+1][j-1] and s[i]==s[j]
        for j in range(1, n):
            for i in range(j):
                # 长度为2
                if j - i == 1:
                    dp[i][j] = True if s[i] == s[j] else False
                else:
                    dp[i][j] = dp[i + 1][j - 1] and (True if s[i] == s[j] else False)
                # 更新
                if dp[i][j] and j - i + 1 > max_len:
                    start = i
                    max_len = j - i + 1
        return s[start:start + max_len]
