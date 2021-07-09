
dp = [[0] * 3] * 4
print(dp)
dp[0][0] = 1
print(id(dp[0][0]), id(dp[1][0]))
print(dp)

a = [[0] * 3 for _ in range(4)]
print(a)
a[0][0] = 1
print(id(a[0][0]), id(a[1][0]))
print(a)
