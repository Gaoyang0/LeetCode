# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float("-inf")

        def bak(root):
            if root:
                l = max(bak(root.left), 0)
                r = max(bak(root.right), 0)

                self.res = max(self.res, l + r + root.val)

                # 返回以root为起点的最大路径
                return max(l, r) + root.val
            else:
                return 0

        bak(root)
        return self.res