class Node:
    def __init__(self, val, key, pre=None, nex=None):
        self.val = val
        self.key = key
        self.pre = pre
        self.nex = nex


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()
        self.head = Node(None, None)
        self.head.pre = self.head
        self.head.nex = self.head


    def get(self, key: int) -> int:
        if key in self.map:
            p = self.map[key]
            # 维护双向链表
            # 断链
            self.remove(p)
            # 头插
            self.insert_head(p)
            return p.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            # 找到并放到前面
            # 找到
            self.map[key].val = value
            p = self.map[key]
            # 断链
            self.remove(p)
            # 头插
            self.insert_head(p)
        else:
            # 头插法
            # 判断是否超过容量
            if len(self.map) >= self.capacity:
                # 删除
                del self.map[self.head.pre.key]
                self.head.pre.pre.nex = self.head
                self.head.pre = self.head.pre.pre

            # 头插
            p = Node(value, key)
            self.insert_head(p)
            self.map[key] = p

    def remove(self, node):
        node.pre.nex = node.nex
        node.nex.pre = node.pre


    def insert_head(self, node):
        node.nex = self.head.nex
        self.head.nex.pre = node
        self.head.nex = node
        node.pre = self.head


# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

l = LRUCache(1)
l.put(2,1)
print(l.map)
print(l.get(2))
print(l.map)
