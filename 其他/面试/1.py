N = int(input().strip())
msg = [i for i in map(int, input().strip().split(" "))]

mat = []
for i in range(0, len(msg), N):
    mat.append(msg[i:i+N])

# 初始化
res = mat[0][0]
# 三层循环
for i in range(N):
    total = [0] * N
    for j in range(i, N):
        cur_max = 0
        for k in range(N):
            total[k] += mat[j][k]
            if cur_max > 0:
                # 加上
                cur_max += total[k]
            else:
                cur_max = total[k]
            # 更新
            res = max(cur_max, res)

print(res)
