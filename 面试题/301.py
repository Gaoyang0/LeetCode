from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def calculate_delete_num(s):
            # 遍历一次计算多余的左右括号数
            l_num, r_num = 0, 0
            '''如果当前遍历到的左括号的数目严格小于右括号的数目则表达式无效。'''
            for ch in s:
                if ch == "(":
                    l_num += 1
                elif ch == ")":
                    # 当l_num为0就表示，此时这个）说明当前遍历到的左括号的数目严格小于右括号的数目==>导致无效
                    if l_num == 0:
                        r_num += 1
                    else:
                        l_num -= 1
            return l_num, r_num

        l_num, r_num = calculate_delete_num(s)
        res = []
        hash_map = set()

        def bak(string, p, surplus_l, surplus_r):
            if surplus_l == 0 and surplus_r == 0:
                l, r = calculate_delete_num(string)
                # 判断是否合法, 去重(哈希表)
                if l + r == 0 and string not in hash_map:
                    hash_map.add(string)
                    return res.append(string)

            if p >= len(string):
                return

            if string[p] == "(":
                if surplus_l > 0:
                    # 删除"("
                    bak(string[:p] + string[p+1:], p, surplus_l-1, surplus_r)
                # 保留"("
                bak(string, p+1, surplus_l, surplus_r)
            elif string[p] == ")":
                if surplus_r > 0:
                    # 删除")"
                    bak(string[:p] + string[p+1:], p, surplus_l, surplus_r-1)
                # 保留")"
                bak(string, p+1, surplus_l, surplus_r)
            else:
                bak(string, p + 1, surplus_l, surplus_r)

        bak(s, 0, l_num, r_num)
        return res


s = Solution()
# print(s.removeInvalidParentheses("()())())"))
# print(s.removeInvalidParentheses(")("))
print(s.removeInvalidParentheses("(a)())()"))