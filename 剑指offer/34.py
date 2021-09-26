from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        # 层次遍历
        if root:
            res = []
            que = [(root, root.val, [root.val])]
            while len(que) > 0:
                node, s, path = que.pop(0)
                if node.left is None and node.right is None and s == target:
                    res.append(path)
                    continue
                if node.left:
                    que.append((node.left, s+node.val, path +[node.val]))

                if node.right:
                    que.append((node.right, s + node.val, path + [node.val]))
            return res


