class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        temp = [""]*numRows
        flag = 1
        index = -1
        for i, char in enumerate(s):
            index += flag
            temp[index] += char
            if index == numRows - 1: flag = -1
            if index == 0: flag = 1
        return "".join(temp)


s = Solution()
print(s.convert("AB", 1))