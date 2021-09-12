n, q = map(int, input().strip().split(" "))

lib_relation = [[] for _ in range(n)]
for i in range(n):
    lines = list(map(int, input().strip().split(" ")))
    if len(lines) == 1:
        lib_relation.append([])
    else:
        for cu in lines[1:]:
            lib_relation[i].append(cu-1)
            lib_relation[cu-1].append(i)


state = {i: False for i in range(n)}
for _ in range(q):
    c, index = map(int, input().strip().split(" "))
    index -= 1
    if c == 1:
        state[index] = True
        s = set([i for i in lib_relation[index]])
        qu = [i for i in lib_relation[index]]
        while len(qu) > 0:
            temp = qu.pop(0)
            state[temp] = True
            for cu in lib_relation[temp]:
                if cu not in s:
                    qu.append(cu)
        print(len([1 for k, v in state.items() if v == True]))
    elif c == 0:
        state[index] = False
        qu = [i for i in lib_relation[index]]
        s = set([i for i in lib_relation[index]])
        while len(qu) > 0:
            temp = qu.pop(0)
            state[temp] = False
            for cu in lib_relation[temp]:
                if cu not in s:
                    qu.append(cu)
        print(len([1 for k, v in state.items() if v == True]))




