from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 问题可以等价为有向图判断有没有环
        # # 拓扑排序
        # # 生成入度表和邻接表
        # in_degrees = [0 for _ in range(numCourses)]
        # adjacency = [[] for _ in range(numCourses)]
        #
        # # 按照点技能树的思路理解pre->cur
        # for cur, pre in prerequisites:
        #     # 要学习cur, 必须先学习pre
        #     # 入度, 表示要学cur, 必须要学入度个前置课程
        #     in_degrees[cur] += 1
        #     # adjacency[pre]存的是必须先学pre的课程
        #     adjacency[pre].append(cur)
        #
        # from collections import deque
        # queue = deque()
        # # 获取所有入度为0的节点, 这些节点没有必须先学的课程
        # for i in range(len(in_degrees)):
        #     if not in_degrees[i]:
        #         queue.append(i)
        #
        # # BFS TopSort
        # node_nums = numCourses
        # while queue:
        #     pre = queue.popleft()
        #     node_nums -= 1
        #     for cur in adjacency[pre]:
        #         # 前置课程减一
        #         in_degrees[cur] -= 1
        #         if not in_degrees[cur]:
        #             queue.append(cur)
        # # 如果存在环，环中节点的入度不能减为0=>不能把所有的节点都入队出队一遍，导致node_nums大于0
        # return not node_nums


        def dfs(i, adjacency, flags):
            '''
            未被 DFS 访问：i == 0
            已被其他节点启动的 DFS 访问：i == -1
            已被当前节点启动的 DFS 访问：i == 1
            '''
            # 被其他节点启动的DFS访问过，直接忽略
            if flags[i] == -1:
                return True
            # 被自己启动的DFS访问过，即有环
            if flags[i] == 1:
                return False
            # 标记是已被自己访问过
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags):
                    return False
            # 标记为访问过，且且无环
            flags[i] = -1
            return True

        # 初始化adjacency和flags
        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)

        for i in range(numCourses):
            # 判断以i为起点的DFS是否有环
            if not dfs(i, adjacency, flags):
                return False
        return True



        # DFS



s = Solution()
print(s.canFinish(2, [[1,0],[0,1]]))
print(s.canFinish(2, [[1,0]]))