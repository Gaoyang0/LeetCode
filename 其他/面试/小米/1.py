x1, y1, z1 = list(map(int, input().strip().split(" ")))
x2, y2, z2 = list(map(int, input().strip().split(" ")))
x3, y3, z3 = list(map(int, input().strip().split(" ")))
x4, y4, z4 = list(map(int, input().strip().split(" ")))

ux = x2 - x1
uy = y2 - y1
uz = z2 - z1

vx = x4-x3
vy = y4-y3
vz = z4-z3

wx = x1-x3
wy=y1-y3
wz = z1-z3

a = ux*ux + uy*uy +uz*uz
b = ux*vx+uy*vy+uz*vz
c = vx*vx+vy*vy+vz*vz
d = ux*wx+uy*wy+uz*wz
e = vx*wx+vy*wy+vz*wz
dt = a*c - b*b
sd = dt
td=dt
sn = 0.0
tn = 0.0


def is_equal(d1, d2):
    if abs(d1-d2) < 0.0000001:
        return True
    else:
        return False

if is_equal(dt, 0):
    sn = 0
    sd = 1
    tn = e
    td = c
else:
    sn = b*e + c*d
    tn = a*e -b *d
    if sn <0:
        sn = 0
        tn = e
        td = c
    elif sn >sd:
        sn = sd
        tn = e+b
        td = c
if tn <0:
    tn = 0
    if -d <0:
        sn = 0
    elif -d > a:
        sn = sd
    else:
        sn = -d
        sd = a
elif tn >td:
    tn = td
    if -d +b <0:
        sn = 0
    elif b-d>a:
        sn = sd
    else:
        sn = b-d
        sd = a

sc = 0
tc =0
if is_equal(sn, 0):
    sc = 0
else:
    tc = tn/td

dx = wx + sc*ux-tc*vx
dy = wy + sc *uy - tc*vy
dz = wz + sc*uz -tc *vz

print(dx*dx + dy*dy +dz*dz)

