class Solution:
    def rec(self , results ):
        # write code here
        res = []
        for line in results:
            res.extend(line)
        res = list(set(res))
        res.sort(reverse=True)
        return res

s = Solution()
print(s.rec([[1,3,2],[4,5,6],[7,5,9]]))