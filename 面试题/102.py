from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        queue = [(root, 0)]
        while (queue.__len__() != 0):
            p, layer = queue.pop(0)
            if len(res) <= layer:
                res.append([])
            res[layer].append(p.val)
            if p.left:
                queue.append((p.left, layer+1))
            if p.right:
                queue.append((p.right, layer+1))
        return res

s = Solution()

r = TreeNode(3, TreeNode(9, None, TreeNode(20, TreeNode(15), TreeNode(7))))
print(s.levelOrder(r))