T = int(input().strip())


class UnionFinSet:
    def __init__(self, data_list):
        self.father_dict = {}
        self.size_dict = {}
        self.count = len(data_list)
        for node in data_list:
            self.father_dict[node] = node
            self.size_dict[node] = 1

    def find(self, node):
        father = self.father_dict[node]
        if  node != father:
            if father != self.father_dict[father]:
                self.size_dict[father] -= 1
            father = self.find(father)
        self.father_dict[node] = father
        return father

    def union(self, a, b):
        if a is None or b is None:
            return
        a_head = self.find(a)
        b_head = self.find(b)
        if a_head != b_head:
            self.count -= 1
            a_set_size = self.size_dict[a_head]
            b_set_size = self.size_dict[b_head]
            if a_set_size >= b_set_size:
                self.father_dict[b_head] = a_head
                self.size_dict[a_head] = a_set_size + b_set_size
            else:
                self.father_dict[a_head] = a_head
                self.size_dict[b_head] = a_set_size + b_set_size


def fun(n, arr):
    parent = range(n)
    uf = UnionFinSet(parent)
    for a, b in arr:
        uf.union(a, b)
    return uf.count


for _ in range(T):
    n, m = map(int, input().strip().split(" "))
    arr = []
    for _ in range(m):
        a, b = map(int, input().strip().split(" "))
        arr.append([a, b])
    print(fun(n, arr)+1)



