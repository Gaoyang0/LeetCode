n, first, second = map(int, input().strip().split(" "))
people = [i for i in range(1, n+1)]


print(3, 4)


min_res = n
max_res = 0
def fun(cur, num):
    global min_res, max_res

    split_res = []
    for i in range((len(cur)) // 2):
        a, b = cur[i], cur[len(cur)-1-i]
        if (a == first and b == second) or (a == second and b == first):
            min_res = min(min_res, num+1)
            max_res = max(max_res, num+1)
            return
        split_res.append([a, b])
    # if len(cur) % 2 != 0:
    #     split_res.append([cur[(len(cur)) // 2]])

    res = []
    for ab in split_res:
        if first in ab or second in ab:
            continue
        res.append([ab[0], ab[1]])


    for a, b in res:








