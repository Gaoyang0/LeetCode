# 牛顿迭代法

def fun2(k):
    def f(x):
        return x**2 - k

    def d_f(x):
        return 2*x

    p0 = 1
    for i in range(1000):
        p = p0 - f(p0) / d_f(p0)
        if abs(p - p0) < 0.00001:
            return p
        p0 = p
    return -1


print(fun2(10))





# 梯度下降
def fun(a):
    y = lambda x : x**2
    dy_dx = lambda x: 2*x
    def get_dx(x):
        loss = abs(a - y(x))
        return loss * dy_dx(x)

    x = 1
    lr = 0.0001
    for _ in range(20000):
        x += lr * get_dx(x)
    return x


# 二分法
def fun1(x):
    l, h = 0, x/2
    while True:
        mid = (l+h) / 2
        if abs(mid ** 2 - x) < 0.00001:
            return mid
        elif mid ** 2 < x:
            l = mid
        elif mid ** 2 > x:
            h = mid

print(fun(10))