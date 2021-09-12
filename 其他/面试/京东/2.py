n, q = map(int, input().strip().split(" "))

lib_relation = []
for i in range(n):
    lines = list(map(int, input().strip().split(" ")))
    if len(lines) == 1:
        lib_relation.append([])
    else:
        lib_relation.append([i-1 for i in lines[1:]])

lib_relation_re = [[] for _ in range(n)]
for i, items in enumerate(lib_relation):
    for j in items:
        lib_relation_re[j].append(i)

def fun(flag, index):
    global state
    cur = True if flag == 1 else False
    state[index] = cur
    cur_re = lib_relation if flag == 1 else lib_relation_re
    s = set([i for i in cur_re[index]])
    qu = [i for i in cur_re[index]]
    while len(qu) > 0:
        temp = qu.pop(0)
        state[temp] = cur
        for cu in cur_re[temp]:
            if cu not in s:
                qu.append(cu)
    return len([1 for k, v in state.items() if v == True])

state = {i: False for i in range(n)}
for _ in range(q):
    c, index = map(int, input().strip().split(" "))
    index -= 1
    print(fun(c, index))





