# from typing import List
#
#
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         n = len(nums)
#
#         def back(i, tmp):
#             res.append(tmp)
#             for j in range(i, n):
#                 # 在已选的基础上再选一个
#                 back(j + 1, tmp + [nums[j]])
#
#         back(0, [])
#         return res
#
#
# s = Solution()
# print(s.subsets([1, 2, 3]))
#
# for i in range(1, 1):
#     print(i)
#
#
# d = {1:2, 4:2}
# print(d)
# for k, v in d.items():
#     if k == 1:
#         d[4] = 3
#     print(d)

# from time import time
#
#
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# listb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.01]
# t = time()
# for i in range(1000000):
#     for a in range(len(lista)):
#         for b in range(len(listb)):
#             x = lista[a] + listb[b]
# print("total run time:", time() - t)
#
# t = time()
# len1 = len(lista)
# len2 = len(listb)
# for i in range(1000000):
#     for a in range(len1):
#         temp = lista[a]
#         for b in range(len2):
#             x = temp + listb[b]
# print("total run time:", time() - t)
#
# # total run time: 35.94349479675293
# # total run time: 29.186986684799194


# from time import time
#
#
# abbreviations = ['cf.', 'e.g.', 'ex.', 'etc.', 'fig.', 'i.e.', 'Mr.', 'vs.']
# t = time()
# for i in range(1000000):
#     for w in ('Mr.', 'Hat', 'is', 'chasing', 'the', 'black', 'cat', '.'):
#         if w in abbreviations:
#             pass
# print("total run time:", time() - t)
#
# t = time()
# for i in range(1000000):
#     for w in ('Mr.', 'Hat', 'is', 'chasing', 'the', 'black', 'cat', '.'):
#         if w[-1] == '.' and w in abbreviations:
#             pass
# print("total run time:", time() - t)
#
# # total run time: 2.915415048599243
# # total run time: 2.210136651992798

# from time import time
#
# t = time()
# list = ['a', 'b', 'is', 'python', 'jason', 'hello', 'hill', 'with', 'phone', 'test',
#         'dfdf', 'apple', 'pddf', 'ind', 'basic', 'none', 'baecr', 'var', 'bana', 'dd', 'wrd']
# total = []
# for i in range(1000000):
#     for w in list:
#         total.append(w)
# print("total run time:", time() - t)
#
# t = time()
# for i in range(1000000):
#     total = [w for w in list]
# print("total run time:", time() - t)
# # total run time: 2.5990912914276123
# # total run time: 0.8667190074920654

import profile


def profileTest():
    Total = 1
    for i in range(10):
        Total = Total * (i + 1)
        print(Total)
    return Total


if __name__ == "__main__":
    # profile.run("profileTest()")

    print(2e-2)