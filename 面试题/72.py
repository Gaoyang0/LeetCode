class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''问题转化及分析
        对word1，word2从后向前扫描
        如果word1[i], word2[j]相等，则该问题可转化为计算word1[0, 1, ..., i-1], word2[0, 1, ..., j-1]的最短编辑距离
        如果word1[i], word2[j]不相等，按照题目提供的操作有三种情况：
        1. 插入，相当于在word1后面插入word2[j]，则该问题可转化为计算word1[0, 1, ..., i], word2[0, 1, ..., j-1]的最短编辑距离
        2. 删除，相当于删除word1最后一个字符，则该问题可转化为计算word1[0, 1, ..., i-1], word2[0, 1, ..., j]的最短编辑距离
        3. 替换，想相当于将word1最后一个字符换为word2[j], 则该问题可转化为计算word1[0, 1, ..., i-1], word2[0, 1, ..., j-1]的最短编辑距离
        '''
        # # 递归
        # # 递归有重复的计算操作，超时
        # # 递归出口
        # # 当word1的长度为0的时候，只需要插入len(word2)次
        # # 当word2的长度为0的时候，只需要删除len(word1)次
        # if len(word1) == 0 or len(word2) == 0:
        #     return max(len(word1), len(word2))
        #
        # # word1[i], word2[j]相等
        # if word1[-1] == word2[-1]:
        #     return self.minDistance(word1[:-1], word2[:-1])
        # else:
        #     insert = self.minDistance(word1, word2[:-1])
        #     delete = self.minDistance(word1[:-1], word2)
        #     replace = self.minDistance(word1[:-1], word2[:-1])
        #     return min(insert, delete, replace) + 1

        # 动态规划
        # 状态转移方程
        # if word1[i] == word2[j] ==> dp[i][j] = dp[i-i][j-1]
        # if word1[i] != word2[j] ==> dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-i][j-1]) + 1

        # 构造初始解相当于递归出口dp[i][0] = i, dp[0][j] = j
        n = len(word1)
        m = len(word2)

        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # DP 数组
        D = [[0] * (m + 1) for _ in range(n + 1)]

        # 边界状态初始化
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j

        # 状态转移
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                insert = D[i][j - 1]
                delete = D[i - 1][j]
                replace = D[i - 1][j - 1]
                if word1[i - 1] == word2[j - 1]:
                    D[i][j] = D[i - 1][j - 1]
                else:
                    D[i][j] = min(insert, delete, replace) + 1
        return D[-1][-1]






s = Solution()
print(s.minDistance("horse", "ros"))