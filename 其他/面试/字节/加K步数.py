a, b = map(int, input().strip().split(" "))

def fun(a, b):
    if a < b:
        a, b = b, a
    k = 1

    while b + k < a:
        b += k
        k += 1

    if a == b + k:
        print(k)
    else:
        diff = a - b
        for i in range(1, 1000):
            if (i*i - diff)%2 == 0:
                print(i * 2 + k-1)
                break

fun(a, b)

