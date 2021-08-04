
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x ^ y
        b = bin(x)
        c = bin(y)
        print(type(a), type(b), type(c))
        return bin(x ^ y).count('1')

s = Solution()
print(s.hammingDistance(1, 4))