class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口
        if s == "":
            return 0
        l = r = 0
        ss = set()
        res = 1
        while len(s) > r >= l:
            if s[r] not in ss:
                ss.add(s[r])
                r += 1
                if r-l > res:
                    res = r-l
            else:
                for i in range(l, r):
                    ss.remove(s[i])
                    if s[i] == s[r]:
                        l = i + 1
                        break
                ss.add(s[r])
                r += 1
        return res





s = Solution()
# print(s.lengthOfLongestSubstring("abcabcbb"))
# print(s.lengthOfLongestSubstring("bbbbbbbbb"))
# print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring(""))
print(s.lengthOfLongestSubstring("a"))
print(s.lengthOfLongestSubstring(" "))
print(s.lengthOfLongestSubstring("au"))