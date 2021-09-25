R = int(input().strip())
N = int(input().strip())

edges = []
for _ in range(N):
    a, b = map(int, input().strip().split(" "))
    edges.append([a, b])

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist(p1, p2):
    return math.sqrt(math.pow(p1.x-p2.x, 2) + math.pow(p1.y - p2.y, 2))


def get_center(p1, p2):
    mid = Point((p1.x + p2.x)/2, (p1.y + p2.y)/2)
    angle = math.atan2(abs(p1.x-p2.x), abs(p2.y-p1.y))
    d = math.sqrt(R*R - math.pow(dist(p1, mid), 2))
    return Point(mid.x + d*math.cos(angle), mid.y-d*math.sin(angle)), Point(mid.x - d*math.cos(angle), mid.y+d*math.sin(angle))


def fun():

    res = dict()
    for i in range(len(edges)):
        for j in range(i+1, len(edges)):
            p1, p2 = Point(edges[i][0], edges[i][1]), Point(edges[j][0], edges[j][1])
            if dist(p1, p2) > 2.0*R:
                continue
            center1, center2 = get_center(p1, p2)
            cnt1 = 0
            cnt2 = 0
            for k in range(len(edges)):
                pk = Point(edges[k][0], edges[k][1])
                if dist(center1, pk) <= 1.0*R:
                    cnt1 += 1
                if dist(center2, pk) <= 1.0*R:
                    cnt2+=1


            if cnt1 not in res:
                res[cnt1] = []
            res[cnt1].append([int(center1.x), int(center1.y)])
            if cnt2 not in res:
                res[cnt2] = []
            res[cnt2].append([int(center2.x), int(center2.y)])

    r = max(res.keys())
    return res[r]
res = fun()

res= sorted(res, key=lambda x:x[0], reverse=False)

print(" ".join(map(str, res[-1])))