# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # self.temp = float("-inf")
        # def traverse(root):
        #     if root:
        #         l = traverse(root.left)
        #         print(root.val)
        #         if root.val <= self.temp:
        #             return False
        #         self.temp = root.val
        #         r = traverse(root.right)
        #         return r and l
        #     return True
        # return traverse(root)
        self.temp = []
        def traverse(root):
            if root:
                traverse(root.left)
                self.temp.append(root.val)
                traverse(root.right)
        traverse(root)
        for i in range(1, len(self.temp)):
            if self.temp[i-1] >= self.temp[i]:
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
    line = "[5,1,4,null,null,3,6]"
    root = stringToTreeNode(line)

    ret = Solution().isValidBST(root)

    out = (ret)
    print(out)



if __name__ == '__main__':
    main()