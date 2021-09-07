class Solution:
    def fun(self, s):
        self.res = 0
        flag = "STAR"

        def bak(cur, i):
            if i >= len(s):
                return
            if len(cur) == 4:
                self.res += 1
                return
            for index in range(i, len(s)):
                if s[index] == flag[len(cur)]:
                    if len(cur) > 0:
                        if cur[-1][1] != index - 1:
                            cur.append([s[index], index])
                            bak(cur, i + 1)
                            cur.pop()
                    else:
                        cur.append([s[index], index])
                        bak(cur, i + 1)
                        cur.pop()
        bak([], 0)
        return self.res


s = Solution()
print(s.fun("SSTTAARR"))
print(s.fun("SSTAARR"))
