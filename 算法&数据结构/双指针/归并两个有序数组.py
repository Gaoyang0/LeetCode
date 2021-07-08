# leetcode 524

from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # 判断s1是否在s2中
        def flag(s1, s2):
            p1, p2 = 0, 0
            while p1 < len(s1) and p2 < len(s2):
                if s1[p1] == s2[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    p2 += 1

            if p1 == len(s1):
                return True
            else:
                return False
        max_len, max_index = -1, -1
        for index, item in enumerate(dictionary):
            if flag(item, s):
                if len(item) > max_len or (len(item) == max_len and dictionary[max_index] > item):
                    max_len = len(item)
                    max_index = index

        if max_index == -1:
            return ""
        else:
            return dictionary[max_index]



s = Solution()
print(s.findLongestWord(s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]))