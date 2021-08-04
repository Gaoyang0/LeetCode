# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        self.res = 0
        def traverse(root):
            if root is not None:
                l = traverse(root.left)
                r = traverse(root.right)
                l.extend(r)
                s = [root.val + i for i in l] + [root.val]
                for i in s:
                    if i == targetSum:
                        self.res += 1
                return [root.val] if len(l) == 0 else s
            else:
                return []

        traverse(root)
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

    line = "[10,5,-3,3,2,null,11,3,-2,null,1]"
    root = stringToTreeNode(line)
    line = "8"
    targetSum = int(line)

    ret = Solution().pathSum(root, targetSum)

    out = str(ret)
    print(out)



if __name__ == '__main__':
    main()