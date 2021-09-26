from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:

        l = len(s)
        res = set()
        def bak(cur, can):
            if len(cur) == l:
                res.add("".join(cur))
                return
            for i in can.copy():
                cur.append(i)
                can.remove(i)
                bak(cur, can)
                can.append(i)
                cur.pop(-1)
        bak([], list(s))
        return list(res)




s = Solution()
print(s.permutation("aab"))