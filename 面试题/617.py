# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # 先序遍历
        def fun(root1: TreeNode, root2: TreeNode, root: TreeNode, flag):
            if root1 != None and root2 != None:
                root1.val += root2.val
                fun(root1.left, root2.left, root1, "l")
                fun(root1.right, root2.right, root1, "r")
            elif root1 != None and root2 == None:
                fun(root1.left, None, root1, "l")
                fun(root1.right, None, root1, "r")
            elif root1 == None and root2 != None:
                temp = TreeNode(root2.val)
                if flag == 'l':
                    root.left = temp
                else:
                    root.right = temp
                fun(temp.left, root2.left, temp, "l")
                fun(temp.right, root2.right, temp, "r")
            return root1
        if root1 == None:
            return root2
        elif root2 == None:
            return root1
        return fun(root1, root2, None, '')


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


    line = "[9, -1, null, -2, 0, -4, null, null, 8, -5, -3, 6, null, null, null, null, null, null, 7]"
    root1 = stringToTreeNode(line)
    line = "[-1, -2, 0, null, null, null, 8, 6, null, null, 7]"
    root2 = stringToTreeNode(line)

    ret = Solution().mergeTrees(root1, root2)

    out = treeNodeToString(ret)
    print(out)



if __name__ == '__main__':
    main()