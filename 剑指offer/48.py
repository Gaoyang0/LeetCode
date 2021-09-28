class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i)   # 更新左指针 i
            dic[s[j]] = j               # 哈希表记录
            res = max(res, j - i)       # 更新结果
        return res

        # res = 0
        # l, r = 0, 1
        # dic = dict()
        # dic[s[0]] = 0
        # while l <= r < len(s):
        #     while r < len(s) and s[r] not in dic.keys():
        #         dic[s[r]] = r
        #         r += 1
        #     res = max(res, r-l)
        #     mid = dic[s[r]]
        #     for i in range(l, mid+1):
        #         del dic[s[i]]
        #     dic[s[r]] = r
        #     l = mid + 1
        #     r += 1
        #
        # return res



        # res = 0
        # for i in range(len(s)):
        #     dic = set()
        #     dic.add(s[i])
        #     for j in range(i+1, len(s)):
        #         if s[j] in dic:
        #             res = max(res, j-i)
        #             break
        #         else:
        #             res = max(res, j - i+1)
        #             dic.add(s[j])
        # return res


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("qu"))
