
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 等价为max(节点的左子树层数+节点的右子树层数)
        self.res = 0
        def deep(root):
            if root == None:
                return 0
            l = deep(root.left) + 1
            r = deep(root.right) + 1
            self.res = max(l + r-2, self.res)
            return max(l,r)
        deep(root)
        return self.res


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
    line = "[3,1,null,null,2]"
    root = stringToTreeNode(line)

    ret = Solution().diameterOfBinaryTree(root)

    out = str(ret)
    print(out)



if __name__ == '__main__':
    main()