n, m = map(int, input().strip().split(" "))

edges = dict()
for _ in range(m):
    a, b = map(int, input().strip().split(" "))
    if a not in edges:
        edges[a] = set()
    edges[a].add(b)

    if b not in edges:
        edges[b] = set()
    edges[b].add(a)

# print(edges)

class S:
    def fun(self):
        self.res = 0
        r = []
        nodes = [i+1 for i in range(n)]

        def bak(cur: set, i):
            if len(cur) == 5:
                temp = list(cur)
                temp.sort()
                r.append(tuple(temp))
                return

            if i >= len(nodes):
                return
            for nex in edges[nodes[i]]:
                if nex not in cur:
                    cur.add(nex)
                    bak(cur, i+1)
                    cur.remove(nex)
        for i in nodes:
            bak(set([i]), 0)
        print(len(set(r)))
        return self.res

s = S()
s.fun()