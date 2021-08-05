# Definition for a binary tree node.
import json
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        root = TreeNode(preorder[0])
        cut = inorder.index(preorder[0])
        if cut > 0:
            root.left = self.buildTree(preorder[1:1+cut], inorder[:cut])
        if 1+cut < len(preorder) and 1+cut < len(inorder):
            root.right = self.buildTree(preorder[1+cut:], inorder[1+cut:])
        return root


def stringToIntegerList(input):
    return json.loads(input)


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def main():

    line = "[3,9,20,15,7]"
    preorder = stringToIntegerList(line)
    line = "[9,3,15,20,7]"
    inorder = stringToIntegerList(line)

    ret = Solution().buildTree(preorder, inorder)

    out = treeNodeToString(ret)
    print(out)



if __name__ == '__main__':
    main()