# while True:
N, K = map(int, input().strip().split(" "))

msg = [i for i in map(int, input().strip().split(" "))]

inf = float("inf")
roads = [[inf] * N for _ in range(N)]

for i in range(0, len(msg), 3):
    a, b, c = msg[i], msg[i+1], msg[i+2]
    roads[a-1][b-1] = c
    roads[b-1][a-1] = c


def floyd(d):
    n = len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d

res = 0
d = floyd(roads)
for i in range(N):
    for j in range(i+1, N):
        if d[i][j] <= K:
            res += 1

print(res)

# def get_min_path(start, graph):
#     passed = [start]
#     nopass = [i for i in range(len(graph)) if i != start]
#     dis = graph[start]
#
#     while len(nopass):
#         idx = nopass[0]
#         for i in nopass:
#             if dis[i] < dis[idx]:
#                 idx = i
#
#         nopass.remove(idx)
#         passed.append(idx)
#
#         for i in nopass:
#             if dis[idx] + graph[idx][i] < dis[i]:
#                 dis[i] = dis[idx] + graph[idx][i]
#     return dis

# res = 0
# for i in range(N):
#     s = set(range(i+1, N))
#     dis = get_min_path(i, roads)
#     print(dis)
#     for index, min_path in enumerate(dis):
#         if min_path <= K and index in s:
#             res += 1
# print(res)

