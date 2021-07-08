import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def flag(d):
            for v in d.values():
                if v > 0:
                    return False
            return True

        t_d = collections.defaultdict(int)
        for i in t:
            t_d[i] += 1

        min_len = len(s) + 1
        min_str = ""
        r = 0
        for l in range(len(s)):
            if s[l] in t:
                # l右移
                while r < len(s) and flag(t_d) == False:
                    if s[r] in t:
                        t_d[s[r]] -= 1
                        if flag(t_d):
                            r += 1
                            break
                    r += 1
                if r - l < min_len and flag(t_d):
                    min_len = r - l
                    min_str = s[l:r]
                t_d[s[l]] += 1
        return min_str



s = Solution()
print("11111111", s.minWindow("a", "aa"))