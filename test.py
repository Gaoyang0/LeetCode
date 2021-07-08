# import os
# os.chdir(os.path.split(os.path.realpath(__file__))[0])
#
# import sys
# sys.path.append(os.path.abspath(".."))
#
#
# from random import random
# from typing import Callable, Iterable
#
#
# def gradient_decent(fn: Callable, partial_derivatives: Iterable[Callable], n_variables: int,
#                     lr=0.1, max_iter=10000, tolerance=1e-5) -> tuple:
#     """Given a function y = f(theta), minimize y by gradient decent method.
#     Args:
#         fn (Callable): The function to optimize.
#         partial_derivatives (Iterable[Callable]): The first partial derivatives of y.
#         n_variables (int): Number of variables.
#         lr (float, optional): Learning rate. Defaults to 0.1.
#         max_iter (int, optional): Max number of iteration. Defaults to 10000.
#         tolerance (float, optional): Defaults to 1e-5.
#     Returns:
#         tuple: Theta, y.
#     """
#     theta = [random() for _ in range(n_variables)]
#     y_cur = fn(*theta)
#     for i in range(max_iter):
#         print("%d iteration, y is %.3f" % (i, y_cur))
#         # Calculate gradient of current theta.
#         gradient = [f(*theta) for f in partial_derivatives]
#         # Update the theta by the gradient.
#         for j in range(n_variables):
#             theta[j] -= gradient[j] * lr
#         # Check if converged or not.
#         y_cur, y_pre = fn(*theta), y_cur
#         if abs(y_pre - y_cur) < tolerance:
#             break
#     return theta, y_cur
#
#
# def f(x, y):
#     # return (x + y - 3) ** 2 + (x + 2 * y - 5) ** 2 + 2
#     return y - x**2 + 4*x
#
#
# def df_dx(x, y):
#     # return 2 * (x + y - 3) + 2 * (x + 2 * y - 5)
#     return -2 * x + 4
#
#
# def df_dy(x, y):
#     # return 2 * (x + y - 3) + 4 * (x + 2 * y - 5)
#     return 1
#
#
# def main():
#     print("Solving the minimum value of quadratic function:")
#     n_variables = 2
#     theta, f_theta = gradient_decent(f, [df_dx, df_dy], n_variables)
#     theta = [round(x, 3) for x in theta]
#     print("The solution is: theta %s, f(theta) %.2f.\n" % (theta, f_theta))
#
#
# if __name__ == "__main__":
#     main()

print("abc" < "abe")