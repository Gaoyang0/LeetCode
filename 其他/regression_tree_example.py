import os
# os.chdir() 方法用于改变当前工作目录到指定的路径。
os.chdir(os.path.split(os.path.realpath(__file__))[0])

import sys
# 添加搜索目录
sys.path.append(os.path.abspath(".."))


from regression_tree import RegressionTree

from utils.load_data import load_boston_house_prices
from utils.model_selection import get_r2, train_test_split
from utils.utils import run_time


@run_time
def main():
    """Tesing the performance of RegressionTree
    """
    print("Tesing the performance of RegressionTree...")
    # Load data
    data, label = load_boston_house_prices()
    # (506, 13)(506, )

    # Split data randomly, train set rate 70%
    data_train, data_test, label_train, label_test = train_test_split(
        data, label, random_state=200)

    # print(data_train.shape, data_test.shape)
    # (354, 13)(152, 13)

    # Train model
    reg = RegressionTree()
    reg.fit(data=data_train, label=label_train, max_depth=5)
    # Show rules
    print(reg)

    # Model evaluation
    get_r2(reg, data_test, label_test)


if __name__ == "__main__":
    main()