k, b = 2, 2


def f(x):
    # f的方程
    return x ** k + x - b


def f_first_order(x):
    # f的一阶导数
    return k * x **(k-1) + 1


def get_root(x0, max_iter=50, tol = 1e-5):
    # 将初始值浮点化
    p0 = x0 * 1.0
    for i in range(max_iter):

        # f的一阶导数不能为0，最普遍的说法是不能非正定
        p = p0 - f(p0)/ f_first_order(p0)

        # 如果小于精度值则退出迭代
        if abs(p - p0) < tol:
            return p
        p0 = p

    return -1

print(get_root(4, 1000))

