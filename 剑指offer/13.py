class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # def dfs(i, j, si, sj):
        #     # 剪枝
        #     if i >= m or j >= n or k < si + sj or (i, j) in visited:
        #         return 0
        #     visited.add((i, j))
        #     left = dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj)
        #     right = dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)
        #     return 1 + left + right
        # visited = set()
        # return dfs(0, 0, 0, 0)

        queue, visited = [(0, 0, 0, 0)], set()
        while queue:
            i, j, si, sj = queue.pop(0)
            # 剪枝
            if i >= m or j >= n or k < si + sj or (i, j) in visited:
                continue
            visited.add((i, j))

            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))
        return len(visited)


s = Solution()

print(s.movingCount(20, 20, 10))