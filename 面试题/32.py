class Solution:
    def longestValidParentheses(self, s: str) -> int:

        if not s:
            return 0
        res = 0
        # -1用于辅助计算长度
        stack = [-1]
        l = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                # -1都出栈了
                if not stack:
                    # 表示字符i没有与之匹配的，以i作为分隔继续寻找
                    # 此时i充当-1的作用
                    stack.append(i)
                else:
                    l = i - stack[-1]
                    res = max(res, l)
        return res

        # # 动态规划
        # # dp[i]表示以s[i]为结尾的字符串,最长有效括号的长度
        # if not s:
        #     return 0
        # dp = [0] * len(s)
        # for i in range(len(s)):
        #     # s[i]为(的时候, dp[i]直接为0
        #     if s[i] == ")":
        #         # 有与s[i]对应的(
        #         if i-dp[i-1]-1 >=0 and s[i-dp[i-1]-1] == "(":
        #             if i-dp[i-1]-2 >= 0:
        #                 # 内部=dp[i-dp[i-1]], 与i对应的(=2, 对应的前面=dp[i-dp[i-1]-2]
        #                 dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
        #             else:
        #                 dp[i] = dp[i - 1] + 2
        #         # 有与s[i]对应的(的时候dp[i]=0, 与初始化的0一致, 所以忽略
        # return max(dp)






s = Solution()
# print(s.longestValidParentheses("(()"))
# print(s.longestValidParentheses("()(()"))
# print(s.longestValidParentheses(")(()())"))
# print(s.longestValidParentheses(")()())"))
# print(s.longestValidParentheses("()(())"))
print(s.longestValidParentheses(")("))