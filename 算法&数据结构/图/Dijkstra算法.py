
'''https://zhuanlan.zhihu.com/p/63395403'''

def startwith(start: int, mgraph: list) -> list:
    passed = [start]
    nopass = [x for x in range(len(mgraph)) if x != start]
    dis = mgraph[start]

    while len(nopass):
        idx = nopass[0]
        for i in nopass:
            if dis[i] < dis[idx]: idx = i

        nopass.remove(idx)
        passed.append(idx)

        for i in nopass:
            if dis[idx] + mgraph[idx][i] < dis[i]: dis[i] = dis[idx] + mgraph[idx][i]
    return dis


if __name__ == "__main__":
    inf = 10086
    mgraph = [[0, 1, 12, inf, inf, inf],
              [inf, 0, 9, 3, inf, inf],
              [inf, inf, 0, inf, 5, inf],
              [inf, inf, 4, 0, 13, 15],
              [inf, inf, inf, inf, 0, 4],
              [inf, inf, inf, inf, inf, 0]]

    dis = startwith(0, mgraph)
    print(dis)

    Inf = float('inf')
    Adjacent = [[0, 1, 12, Inf, Inf, Inf],
                [Inf, 0, 9, 3, Inf, Inf],
                [Inf, Inf, 0, Inf, 5, Inf],
                [Inf, Inf, 4, 0, 13, 15],
                [Inf, Inf, Inf, Inf, 0, 4],
                [Inf, Inf, Inf, Inf, Inf, 0]]
    Src, Dst, N = 0, 5, 6


    def dijstra(adj, src, dst, n):
        dist = [Inf] * n
        dist[src] = 0
        book = [0] * n  # 记录已经确定的顶点
        # 每次找到起点到该点的最短途径
        u = src
        for _ in range(n - 1):  # 找n-1次
            book[u] = 1  # 已经确定
            # 更新距离并记录最小距离的结点
            next_u, minVal = None, float('inf')
            for v in range(n):  # w
                w = adj[u][v]
                if w == Inf:  # 结点u和v之间没有边
                    continue
                if not book[v] and dist[u] + w < dist[v]:  # 判断结点是否已经确定了，
                    dist[v] = dist[u] + w
                    if dist[v] < minVal:
                        next_u, minVal = v, dist[v]
            # 开始下一轮遍历
            u = next_u
        return dist[dst]


    res = dijstra(Adjacent, Src, Dst, N)
    print(res)