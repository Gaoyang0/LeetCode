# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    '''BFS'''
    # def serialize(self, root):
    #     """Encodes a tree to a single string.
    #
    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     # 层次遍历
    #     if not root:
    #         return ""
    #
    #     qu = [root]
    #     res = []
    #     while len(qu) > 0:
    #         p = qu.pop(0)
    #         if p:
    #             res.append(str(p.val))
    #             qu.append(p.left)
    #             qu.append(p.right)
    #         else:
    #             res.append("null")
    #     return " ".join(res)
    #
    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
    #
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #     if not data:
    #         return None
    #     nodes = data.split(' ')
    #     root = TreeNode(nodes.pop(0))
    #     qu = [root]
    #     while len(qu) > 0:
    #         p = qu.pop(0)
    #         if len(nodes) > 0:
    #             val = nodes.pop(0)
    #             if val != 'null':
    #                 p.left = TreeNode(val)
    #                 qu.append(p.left)
    #         if nodes:
    #             val = nodes.pop(0)
    #             if val != 'null':
    #                 p.right = TreeNode(val)
    #                 qu.append(p.right)
    #     return root

    '''DFS'''
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return 'null '
        leftserilized = self.serialize(root.left)
        rightserilized = self.serialize(root.right)
        return str(root.val) + ' ' + leftserilized + rightserilized

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(' ')
        root = self.buildTree(data)
        return root

    def buildTree(self, data):
        val = data.pop(0)
        if val == 'null':
            return None
        node = TreeNode(val)
        node.left = self.buildTree(data)
        node.right = self.buildTree(data)
        return node


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def main():
    line = "[3,2,4,3]"
    root = stringToTreeNode(line)

    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))

    print(ans)


if __name__ == '__main__':
    main()
