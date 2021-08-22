import lightgbm as lgb
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

# 加载数据
boston = load_boston()
data = boston.data
target = boston.target

# 切分数据集
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2)

lgb_train = lgb.Dataset(X_train, y_train)
#If this is Dataset for validation, training data should be used as reference.
lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

params = {
    'task': 'train',
    'boosting_type': 'gbdt',  # 设置提升类型
    'objective': 'regression',  # 目标函数
    'metric': {'l2', 'auc'},  # 评估函数
    'num_leaves': 31,  # 叶子节点数
    'learning_rate': 0.05,  # 学习速率
    'feature_fraction': 0.9,  # 建树的特征选择比例
    'bagging_fraction': 0.8,  # 建树的样本采样比例
    'bagging_freq': 5,  # k 意味着每 k 次迭代执行bagging
    'verbose': 1  # <0 显示致命的, =0 显示错误 (警告), >0 显示信息
}


gbm = lgb.train(params, lgb_train, num_boost_round=20, valid_sets=lgb_eval, early_stopping_rounds=5)
import joblib
gbm.save_model('model.txt')
# joblib.dump(lgb, '.lgb.pkl')

y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration)

print('The MSE of prediction is:', mean_squared_error(y_test, y_pred) ** 0.5)
