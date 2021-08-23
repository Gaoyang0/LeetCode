import lightgbm as lgb
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.model_selection import GridSearchCV

# 加载数据
# boston = load_boston()
# data = boston.data
# target = boston.target
# np.savetxt("data.txt", data)
# np.savetxt("target.txt", target)

# data = np.loadtxt("data.txt")
# target = np.loadtxt("target.txt")

train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")


def get_data(data):
    label_ori = data["label_ori"]
    del data['label_log']
    del data['label_ori']
    X = np.array(data)
    y = np.array(label_ori)
    return X, y


X_train, y_train = get_data(train_df)
X_test, y_test = get_data(test_df)

# 切分数据集
# X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2)

lgb_train = lgb.Dataset(X_train, y_train)
# If this is Dataset for validation, training data should be used as reference.
lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

params = {
    'task': 'train',
    'boosting_type': 'gbdt',  # 设置提升类型
    'objective': 'regression',  # 目标函数
    "max_depth": 100,
    'metric': {'l2'},  # 评估函数
    'num_leaves': 31,  # 叶子节点数
    'learning_rate': 0.05,  # 学习速率
    'feature_fraction': 0.9,  # 建树的特征选择比例
    'bagging_fraction': 0.8,  # 建树的样本采样比例
    'bagging_freq': 5,  # k 意味着每 k 次迭代执行bagging
    'verbose': 1  # <0 显示致命的, =0 显示错误 (警告), >0 显示信息
}





gbm = lgb.train(params, lgb_train, num_boost_round=20, valid_sets=lgb_eval, early_stopping_rounds=5)
# cv_results = lgb.cv(params, lgb_train, num_boost_round=1000, nfold=5, stratified=False, shuffle=True, metrics='l2',early_stopping_rounds=50,seed=0)
y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration)
print('The MSE of prediction is:', mean_squared_error(y_test, y_pred) ** 0.5)
