
# https://www.bilibili.com/video/BV13t411v7Fs?p=1
# 并查集应用: 检测图中是否有环

def find_root(index, parent):
    p, layer = index, 0
    while parent[p] != -1:
        p = parent[p]
        layer += 1
    return p, layer


def union_node(u, v, parent):
    u_root, u_layer = find_root(u, parent)
    v_root, v_layer = find_root(v, parent)
    # 根节点一致说明在一个集合
    if u_root == v_root:
        return False
    else:
        # 保证连接后的层数为max(u_layer, v_layer)
        if u_layer >= v_layer:
            parent[v_root] = u_root
        else:
            parent[u_root] = v_root
        return True


def detect_cycle(graph):
    """
    :param graph:
    :return: True--有环, False--无环
    """
    parent = [-1] * 6
    for u, v in graph:
        if not union_node(u, v, parent):
            return True
    return False




graph = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 4], [3, 5]]
# graph = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5]]
res = detect_cycle(graph)

print(res)
