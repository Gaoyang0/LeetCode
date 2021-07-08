

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # 保证num1更长
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        res = ""
        for index, number in enumerate(num2):
            temp = self.single_multiply(num1, int(number)) + "0"*(len(num2) - index - 1)
            res = self.add_str(temp, res)
        return res

    def single_multiply(self, num1, number):
        r = ""
        temp = 0
        for i in range(len(num1)-1, -1, -1):
            product = int(num1[i]) * number + temp
            temp = product // 10
            r = str(product % 10) + r

        if temp > 0:
            r = str(temp) + r
        return r

    def add_str(self, num1, num2):
        i, j = len(num1) - 1, len(num2) - 1
        add = 0
        ans = list()
        while i >= 0 or j >= 0 or add != 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            result = x + y + add
            ans.append(str(result % 10))
            add = result // 10
            i -= 1
            j -= 1
        return "".join(ans[::-1])




s = Solution()
print(s.multiply("568", "17"))
# print(s.single_multiply("568", 0))