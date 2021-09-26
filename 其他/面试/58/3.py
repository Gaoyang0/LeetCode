import numpy as np


def sigmoid(z):
    return 1 / (1+np.exp(-z))

def fun(x):
    w1 = np.array([[0.5,0.7,0.1],[0.3,0.7,0.4],[0.1,0.7,0.4]])
    w2 = np.array([[0.9,0.1,0.5],[0.6,0.7,0.1],[0.8,0.1,0.5]])
    w3 = np.array([0.4,0.9,0.1])
    b1 = np.array([1, 1, 1])
    b2 = np.array([1, 1, 1])
    b3 = np.array([1])

    # x = np.array([[1,1,1], [1,1,1]])

    z1 = np.matmul(x, w1)
    z1 = z1 + b1
    s1 = sigmoid(z1)

    z2 = np.matmul(s1, w2)
    z2 = z2 + b2
    s2 = sigmoid(z2)

    z3 = np.matmul(s2, w3)
    z3 = z3 + b3
    s3 = sigmoid(z3)
    return s3

lines = input().strip().split("|")
x = []
for line in lines:
    x.append(list(map(int, line.split(","))))
x = np.array(x)
res = fun(x)
for r in res:
    print(r)