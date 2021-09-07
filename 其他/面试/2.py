#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


class Solution:
    def partitionNumber(self, text):
        # Write Code Here
        def fun(text):
            n = len(text)
            for i in range(1, n//2 + 1):
                if text[:i] == text[n-i:n]:
                    return 2 + fun(text[i:n-i])
            return 0 if n == 0 else 1
        s = text
        n = len(s)
        f = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1] or fun(s[i:j + 1]) > 1
        ret, ans = [], []

        def dfs(i):
            if i == n:
                ret.append(ans[:])
                return
            for j in range(i, n):
                if f[i][j]:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)

        return len(ret)


try:
    _text = input()
except:
    _text = None

s = Solution()
res = s.partitionNumber(_text)

print(str(res) + "\n")