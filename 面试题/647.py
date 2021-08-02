class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        # 中心扩散
        # 回文中心为一个字符
        res = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                r += 1
                l -= 1
                res += 1
        # 回文中心为2个字符
        for i in range(len(s) - 1):
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                r += 1
                l -= 1
                res += 1
        return res
        '''

        '''动态规划'''




s = Solution()
print(s.countSubstrings("aaa"))
