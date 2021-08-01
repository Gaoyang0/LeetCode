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
        if node.lchild:
            s1.append(node.lchild)
        if node.rchild:
            s1.append(node.rchild)
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


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


