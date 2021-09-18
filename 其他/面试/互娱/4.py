n, m = map(int, input().strip().split(" "))

users_id2name = dict()
users_name2id = dict()

for _ in range(n):
    id, name = input().strip().split(" ")
    users_id2name[id] = name
    users_name2id[name] = id

rec = []
for _ in range(m):
    uid, aid, score = input().strip().split(" ")
    rec.append([uid, aid, int(score)])


d = dict()
for uid, aid, score in rec:
    if uid not in d:
        d[uid] = [0, set()]
    d[uid][0] += score
    d[uid][1].add(aid)


a = dict()
for uid in d.keys():
    if len(d[uid][1]) >= 2:
        a[uid] = d[uid]

for uid in a.keys():
    a[uid].append(users_id2name[uid])

res = []
for k, v in a.items():
    res.append([v[2], v[0]])


res = sorted(res, key=lambda x:x[1], reverse=True)

dc = dict()
for name, s in res:
    if s not in dc:
        dc[s] = []
    dc[s].append((name, s))

ac = dict()
for key, v in dc.items():
    if len(v) > 1:
        ac[key] = v

s =set()
for i in range(len(res)):
    if res[i][0] not in s:

        if res[i][1] in ac:
            temp = ac[res[i][1]]
            temp = sorted(temp, key=lambda x:x[0], reverse=True)
            for n, c in temp:
                print(n + " " + str(c))
                s.add(n)
            del ac[res[i][1]]
        else:
            s.add(res[i][0])
            print(res[i][0] + " " + str(res[i][1]))


