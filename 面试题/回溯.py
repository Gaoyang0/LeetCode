# from typing import List
#
#
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         # 预处理
#         mapping = {
#             '2':['a','b','c'],
#             '3':['d','e','f'],
#             '4':['g','h','i'],
#             '5':['j','k','l'],
#             '6':['m','n','o'],
#             '7':['p','q','r','s'],
#             '8':['t','u','v'],
#             '9':['w','x','y','z']
#             }
#
#         res = []
#
#         # 回溯
#
#         def back(s, pos, r):
#             # 剪枝判断
#             # 不需要剪枝
#
#             if pos > len(s) -1:
#                 return
#
#             # 目标解判断
#             if pos == len(s) - 1:
#                 for item in mapping[s[pos]]:
#                     res.append(r + item)
#
#             # 循环遍历所有分支
#             for item in mapping[s[pos]]:
#                 back(s, pos+1, r+item)
#
#         back(digits, 0, "")
#
#         return res
#
# s = Solution()
# print(s.letterCombinations(""))


# print(r"\n") # 打印为:\n, 而不是换行

# # 字典排序
# d = {"a": 2, "c": 1, "b": 3}
# # 按照key排序
# l = sorted(d.items(), key=lambda i:i[0], reverse=False)
# print(l)
#
# # 按照value排序
# l = sorted(d.items(), key=lambda i:i[1], reverse=False)
# print(l)
#
# # [('a', 2), ('b', 3), ('c', 1)]
# # [('c', 1), ('a', 2), ('b', 3)]


# from collections import Counter
# s = "adgyhgasjhdghgafdghafdhag]asdjlk;;;:;////a"
# res = Counter(s)
# print(dict(res))
# # {'a': 7, 'd': 5, 'g': 6, 'y': 1, 'h': 5, 's': 2, 'j': 2, 'f': 2, ']': 1, 'l': 1, 'k': 1, ';': 4, ':': 1, '/': 4}

# # 过滤
# seq = [-1, -2, 3, 5, -1, -3]
# res = filter(lambda x:x<0, seq)
# print([i for i in res])
# # [-1, -2, -1, -3]

# # 打印时间
# import time
# print("时间戳:", time.time())
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1381419600)))
# # 时间戳: 1615465862.4757388
# # 2021-03-11 20:31:02
# # 2013-10-10 23:40:00

# 自定义异常
# try:
#     for i in range(5):
#         if i > 2:
#             raise Exception("数字大于2")
# except Exception as e:
#     print(e)


# from typing import List
#
#
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#
#         def back(curr, flag):
#             # flag[0]代表"("剩余数量, flag[1]代表")"剩余数量
#
#             # 剪枝
#             if flag[0] < 0 or flag[1] < 0:
#                 return
#
#             if flag[0] ==0 and flag[1] == 0:
#                 res.append(curr)
#
#             # 剪枝+遍历所有情况
#             if flag[0] > 0 and flag[0] <= flag[1]:
#                 back(curr+"(", [flag[0]-1, flag[1]])
#             if flag[1] > 0 and flag[0] <= flag[1]:
#                 back(curr+")", [flag[0], flag[1]-1])
#
#         res = []
#         back("", [n, n])
#         return res
#
#
# s = Solution()
# print(s.generateParenthesis(0))


# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if needle == "":
#             return 0
#
#         for i in range(len(haystack) - len(needle) + 1):
#             flag = True
#             for j in range(len(needle)):
#                 if haystack[i+j] != needle[j]:
#                     flag = False
#                     break
#             if flag:
#                 return i
#         return -1
#
#
# s = Solution()
# print(s.strStr("1a", "a"))

# x = "::"
# print(x.join("abc"))
# print(x.join(["a", "b", "c"]))
# # a::b::c
# # a::b::c

# try:
#     f = open("回溯.py", "r")
# except Exception as e:
#     print(e)
# else:
#     print("无异常")
# finally:
#     f.close()

# # 英文字符串
# print(type(b"ads"))
# # 中文字符串
# print(type("阿达".encode()))
#
# # <class 'bytes'>
# # <class 'bytes'>


# # 单例模式
# class Singleton(object):
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance
#
# a = Singleton()
# b = Singleton()
#
# print(id(a))
# print(id(b))
# # 1458369503872
# # 1458369503872


# import random
#
# a = random.random()
# print(a)
# print(round(a, 2))
#
# # 0.5677502095964958
# # 0.57

# # 不可变数据类型: 数值型, 字符串, 元组
# a = 3
# b = 3
# print(id(a), id(b))
# s1 = "hello"
# s2 = "hello"
# print(id(s1), id(s2))
# # 140704078899040 140704078899040
# # 2104407974320 2104407974320
#
# # 可变数据类型: 列表, 字典
# def f(key, value, dic=dict()):
#     dic[key] = value
#     print(dic)
# f("a", 1)
# f("b", 2)
# f("c", 3, {})
# # 字典是可变数据类型, 前两个函数调用该dic指向的是同一地址
# # {'a': 1}
# # {'a': 1, 'b': 2}
# # {'c': 3}
#
# x = [1, 2]
# y = [1, 2]
# z = x
# print(id(x), id(y), id(z))
# z.pop()
# print(x, z)
# # x, z id一致, 操作z, 相当于操作了x
# # 2276582249856 2276581513472 2276582249856
# # [1] [1]


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        pre_str = self.countAndSay(n - 1)

        temp_i = 0
        temp_s = pre_str[0]
        i = 1
        res = ""

        while i < len(pre_str):
            if pre_str[i] != temp_s:
                res += str(i - temp_i) + temp_s
                temp_i = i
                temp_s = pre_str[i]
            i += 1
        res += str(i - temp_i) + temp_s
        return res


s = Solution()
print(s.countAndSay(5))


print(3 // 2)