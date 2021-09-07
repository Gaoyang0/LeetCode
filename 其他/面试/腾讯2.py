k, b = 2, 2


def f(x):
    return x ** k + x - b


def f_first_order(x):
    return k * x ** (k - 1) + 1


def get_root(x0, max_iter=50, tol=1e-5):
    p0 = x0 * 1.0
    for i in range(max_iter):
        p = p0 - f(p0) / f_first_order(p0)
        if abs(p - p0) < tol:
            return p
        p0 = p
    return -1


point_x = get_root(b, 1000)
if point_x == -1:
    print("无解")
res = point_x ** (k + 1) / (k + 1) + 0.5 * (b - point_x) ** 2
print(res)
