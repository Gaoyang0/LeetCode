grid = []

line = list(map(int, input().strip().split(" ")))
n = len(line)
grid.append(line)
for _ in range(n - 1):
    grid.append(list(map(int, input().strip().split(" "))))


def fun(gird):
    if n == 1:
        return 0

    visited = set()
    visited.add((0, 0))
    que = [(0, 0)]
    step = 0
    while len(que) > 0:
        step += 1
        cnt = len(que)
        for _ in range(cnt):
            a, b = que.pop(0)
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                temp_x, temp_y = a + x, b + y
                if 0 <= temp_x < n and 0 <= temp_y < n and grid[temp_x][temp_y] == 0 and (temp_x, temp_y) not in visited:
                    if temp_x == n - 1 and temp_y == n - 1:
                        return step + 1
                    que.append((temp_x, temp_y))
                    visited.add((temp_x, temp_y))
    return -1


print(fun(grid))
