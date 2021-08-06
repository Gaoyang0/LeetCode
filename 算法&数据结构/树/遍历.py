class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 前序优先遍历
def qianxu(p: TreeNode):
    res = []
    stack = []
    while (stack.__len__() != 0 or p):
        if p:
            res.append(p.val)
            stack.append(p)
            p = p.left
        else:
            p = stack.pop(-1)
            p = p.right
    return res


# 中序优先遍历
def zhongxu(p: TreeNode):
    res = []
    stack = []
    while (stack.__len__() != 0 or p):
        if p:
            stack.append(p)
            p = p.left
        else:
            p = stack.pop(-1)
            res.append(p.val)
            p = p.right
    return res


# 后序优先遍历
def houxu(p: TreeNode):
    res = []
    stack = []
    d = dict()
    while (p or stack.__len__() != 0):
        if p:
            stack.append(p)
            d.update({p.val: 1})
            p = p.left
        else:
            p = stack[-1]
            if d[p.val] == 2:
                stack.pop(-1)
                res.append(p.val)
                p = None
            else:
                # 代表第二次遇见
                d[p.val] = 2
                p = p.right

    return res


def houxu2(root):
    '''
    利用两个栈实现
    '''
    s1 = []
    s2 = []
    s1.append(root)
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    while s2:
        print(s2.pop().value)


# 层次遍历，用队列
def cengci(p: TreeNode):
    res = []
    queue = [p]
    while (queue.__len__() != 0):
        p = queue.pop(0)
        res.append(p.val)
        if p.left:
            queue.append(p.left)
        if p.right:
            queue.append(p.right)
    return res


# 递归
# 先序
def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)


# 中序
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


# 后序
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)





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






if __name__ == "__main__":
    s = "[1,2,3,4,null,6,7]"
    root = stringToTreeNode(s)
    # preorder(root)

    stack = []
    p = root
    res = []
    while len(stack) != 0 or p:
        if p:
            res.append(p.val)
            stack.append(p)
            p = p.left
        else:
            # temp是已经遍历过的root
            # p为None表示left已经为None, 所以该指向right了
            temp = stack.pop(-1)
            p = temp.right
    print("非递归先序", res)

    p = root
    stack = []
    res = []
    while len(stack) != 0 or p:
        if p:
            stack.append(p)
            p = p.left
        else:
            temp = stack.pop(-1)
            res.append(temp.val)
            p = temp.right
    print("非递归中序", res)

    p = root
    res = []
    stack = []
    d_flag = dict()

    while len(stack) != 0 or p:
        if p:
            stack.append(p)
            # 遇见一次
            d_flag[p] = 1
            p = p.left
        else:
            temp = stack[-1]
            # 如果遇见了一次
            if d_flag[temp] == 1:
                p = temp.right
                # 右子树已经遍历了，下次遇见就可以遍历p了
                d_flag[temp] = 2
            else:
                temp = stack.pop(-1)
                res.append(temp.val)
                # p如果命为None的话, 下次循环还会再出栈一个
                p = None
    print("非递归后序", res)



