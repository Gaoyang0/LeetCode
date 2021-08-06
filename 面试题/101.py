class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # def flag(l, r):
        #     if not l and not r:
        #         return True
        #     elif (l and not r) or (not l and r):
        #         return False
        #     elif l and r:
        #         return l.val == r.val and flag(l.left, r.right) and flag(l.right, r.left)
        #
        # if root is None:
        #     return True
        # else:
        #     return flag(root.left, root.right)

        # 非递归写法
        # 对比正常中序和和改造的中序的

        if root == None:
            return True
        stack = [(root.left, root.right)]
        while stack != []:
            left, right = stack.pop()
            if left == None and right == None:
                continue
            if left and right and left.val == right.val:
                # 将左右孩子添加入队列
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True









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

    line = "[1,2,2,3,4,4,3]"
    root = stringToTreeNode(line)

    ret = Solution().isSymmetric(root)

    out = (ret)
    print(out)



if __name__ == '__main__':
    main()