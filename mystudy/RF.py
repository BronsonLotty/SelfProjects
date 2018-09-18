from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
#输入变量
X, y = make_classification(n_samples=10, n_features=4,
                           n_informative=2, n_redundant=0,
                         random_state=0, shuffle=False)
print(type(X),type(y))
clf = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                        max_depth=2, max_features='auto', max_leaf_nodes=None,
               min_impurity_decrease=0.0, min_impurity_split=None,
               min_samples_leaf=1, min_samples_split=2,
               min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
               oob_score=False, random_state=0, verbose=0, warm_start=False)
clf.fit(X, y)
print(clf.feature_importances_)
scores = cross_val_score(clf, X, y)
print(scores.mean())
print(clf.predict([[0, 0, 0, 0]]))








#支持向量机
# Parameters
#  |      ----------
#  |      X : array-like, shape = (n_samples, n_features)
#  |          Test samples.
#  |
#  |      y : array-like, shape = (n_samples) or (n_samples, n_outputs)
#  |          True labels for X.
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
from sklearn.svm import SVC
clf = SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
      decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
       max_iter=-1, probability=False, random_state=None, shrinking=True,
      tol=0.001, verbose=False)
clf.fit(X, y) #doctest: +NORMALIZE_WHITESPACE
print(clf.predict([[-0.8, -1]]))









#XGBoost
import xgboost as xgb
import numpy as np
data = np.random.rand(5,10) # 5 entities, each contains 10 features
label = np.random.randint(2, size=5) # binary target
dtrain = xgb.DMatrix( data, label=label)
param = {'objective':'binary:logistic', 'n_estimators':2,'bst:max_depth':2, 'bst:eta':1, 'silent':1, 'objective':'binary:logistic','nthread':4,'eval_metric': 'auc'}
num_round = 250
params = {
    'booster': 'gbtree',
    'objective': 'binary:logistic',
    'subsample': 0.6,
    'colsample_bytree': 0.8,
    'eta': 0.1,
    'max_depth': 1,
    'min_child_weight': 1,
    'gamma': 0.0,
    'silent': 0,
    'eval_metric': 'error'}
bst = xgb.train(params, dtrain, num_round)
y = bst.predict(dtrain)


