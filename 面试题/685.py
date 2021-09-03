from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        有环 ：构成环形数字1连到2,2连到3,3连到1就是个环
        冲突 ：一个点有两个父节点
        有环无冲突 [[1,2],[2,3],[3,1]]
        有环有冲突 [[1,2],[2,3],[3,1],[4,2]]
        无环有冲突 [[1,2],[1,3],[2,3]]
        '''
        # [1, 2]表示1-->2, 1表示2的根
        # 并查集
        def find_root(index, parent):
            p = index
            while parent[p] != -1:
                p = parent[p]
            return p

        def union_node(u, v, parent):
            u_root = find_root(u, parent)
            v_root = find_root(v, parent)
            if u_root == v_root:
                return False
            else:
                parent[v_root] = u_root
                return True

        node_set = set()
        for u, v in edges:
            node_set.add(u)
            node_set.add(v)

        # 已经有入度了
        in_dict = dict()
        parent = [-1] * (len(node_set) + 1)

        conflict = -1
        for i in range(len(edges)):
            u, v = edges[i]
            if v in in_dict:
                # 冲突
                conflict = v
            else:
                in_dict[v] = []
            in_dict[v].append(u)

            if not union_node(u, v, parent):
                # 得到环
                all_cycle_node = get_cycle_node(u, v, parent)


                all_cycle_node = u_f | v_f

                if conflict != -1:
                    if conflict == v:
                        return [u, v]
                    # 有环且冲突，应该删除环里的边
                    if conflict in all_cycle_node:
                        return [in_dict[conflict][0], conflict]

                for u_last, v_last in edges[i+1:]:
                    if v_last in in_dict:
                        # 有环且冲突，应该删除环里的边
                        return [in_dict[v_last][0], v_last]
                # 有环，无冲突
                return [u, v]
        return [in_dict[conflict][-1], conflict]


s = Solution()
# print(s.findRedundantDirectedConnection([[1,2],[2,3],[3,4],[4,1],[1,5]]))
# print(s.findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]]))
# print(s.findRedundantDirectedConnection([[0,1],[0,2],[1,2]]))
# print(s.findRedundantDirectedConnection([[1,2],[2,3],[3,4],[4,1],[1,5]]))
# 有环无冲突
# print(s.findRedundantDirectedConnection([[1,2],[2,3],[3,1]]))
# 有环有冲突
# print(s.findRedundantDirectedConnection([[1,2],[2,3],[3,1],[4,2]]))
# 无环有冲突
# print(s.findRedundantDirectedConnection([[1,2],[1,3],[2,3]]))
# print(s.findRedundantDirectedConnection([[1,2],[1,3],[4,2]]))
# print(s.findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]]))
# print(s.findRedundantDirectedConnection([[1,2],[1,3],[2,3]]))
print(s.findRedundantDirectedConnection(
[[5,2],[5,1],[3,1],[3,4],[3,5]]))