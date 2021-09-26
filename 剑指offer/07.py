import json
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 出口
        if len(preorder) == 0:
            return None
        mid = preorder[0]
        root = TreeNode(mid)
        if len(preorder) == 1:
            return root

        index = inorder.index(mid)
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])

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

    line = "[3, 9, 20, 15, 7]"
    preorder = stringToIntegerList(line)
    line = "[9, 3, 15, 20, 7]"
    inorder = stringToIntegerList(line)

    ret = Solution().buildTree(preorder, inorder)
    out = treeNodeToString(ret);
    print(out)



if __name__ == '__main__':
    main()