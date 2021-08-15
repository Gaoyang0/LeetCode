class Solution:
    def decodeString(self, s: str) -> str:

        def back(s):
            res = ""
            i = 0
            while i < len(s):
                if s[i].isdigit():
                    # 防止数字是多位数
                    j = i + 1
                    while s[j] != '[':
                        j += 1
                    r, l = back(s[i+1+j-i:])
                    res += r*int(s[i:j])
                    # 移动指针
                    i += l+2+j-i
                elif s[i] == "]":
                    return res, i
                else:
                    res += s[i]
                    i += 1
            return res, i

        return  back(s)[0]





s = Solution()
print(s.decodeString("ds10[a2[c]]afg"))