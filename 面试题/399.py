from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 转化为一个图算法，判断是否有路径
        # 设边a->c表示a/c，问题转化为最短路径上所有边的乘积

        # 构建有向，带权重的图
        # 计算路径
        # 计算路径

        # 构建图
        G = dict()
        for [u, v], r in zip(equations, values):
            if u not in G:
                G[u] = [(u, 1)]
            G[u].append((v, r))
            if v not in G:
                G[v] = [(v, 1)]
            G[v].append((u, 1/r))

        def BFS(u, v):
            '''没有路径返回-1'''
            if u not in G or v not in G:
                return -1

            stack = [(u, 1)]
            flag_set = set()
            while len(stack) != 0:
                node, mid = stack.pop()
                if node == v:
                    return mid
                for n, div in G[node]:
                    if n not in flag_set:
                        stack.append((n, mid*div))
                        flag_set.add(n)
            return -1
        res = []
        for u, v in queries:
            res.append(BFS(u, v))

        return res


s = Solution()
print(s.calcEquation([["a","b"],["b","c"]], [2.0,3.0],  [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))