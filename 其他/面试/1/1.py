N, M = map(int, input().strip().split(" "))

rec = dict()
for _ in range(N*M):
    temp = list(map(int, input().strip().split(" ")))
    rec[temp[0]] = temp[1:]

res = [[0] * (M+2) for _ in range(N+2)]

lu, ru, ld, rd = 0, 0, 0, 0
for id in rec.keys():
    l, u, r, d = rec[id]
    if l == 0 and u == 0:
        lu = id

visited = {lu}
res[1][1] = lu

q = [(lu, 1, 1)]
while len(q) > 0:
    temp, x, y = q.pop()
    visited.add(temp)
    l, u, r, d = rec[temp]
    if l != 0 and l not in visited:
        res[x][y-1] = l
        q.append((l, x, y-1))
    if u != 0 and u not in visited:
        res[x-1][y] = u
        q.append((u, x-1, y))

    if r != 0 and r not in visited:
        res[x][y+1] = r
        q.append((r, x, y+1))

    if d != 0 and d not in visited:
        res[x+1][y] = d
        q.append((d, x+1, y))

for i in range(1, N+1):
    print(" ".join(map(str, res[i][1:M+1])))



