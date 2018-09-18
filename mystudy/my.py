from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
#from sklearn.datasets import make_classification

#coding=utf-8

import numpy as np
import pandas as pd
file_path = r"/Users/xutingxi/Pyprojects/SelfProjects/mystudy/allnew.csv"
data = pd.read_csv(file_path)


mycolumns = np.arange(2,28,1,int)
all_train_data = data.iloc[:,mycolumns]
myindex =79929
table = all_train_data.iloc[2:myindex,:]
table = np.array(table)

myscore = data.iloc[2:myindex,29]
myscore = np.array(myscore)

#输入变量
# X, y = make_classification(n_samples=10, n_features=4,
#                            n_informative=2, n_redundant=0,
#                          random_state=0, shuffle=False)

print(type(table),type(myscore))
clf = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                             max_depth=10, max_features='auto', max_leaf_nodes=None,
                             min_impurity_decrease=0.0, min_impurity_split=None,
                             min_samples_leaf=1, min_samples_split=2,
                             min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
                             oob_score=False, random_state=0, verbose=0, warm_start=False)
clf.fit(table, myscore)
#print(clf.feature_importances_)
scores = cross_val_score(clf, table, myscore)
print(scores.mean())
#print(clf.predict([[0.8,0.449,0.8,0.8,0.8,0.8,0.8,0.8,0.449,0.8,0.8,0.8,0.8,0.8]]))


all_test_data = data.iloc[:,mycolumns]

test = all_test_data.iloc[myindex:,:]
test = np.array(test)

myture = data.iloc[myindex:,29]
myture = np.array(myture)

mypredect = clf.predict(test)

myerror = mypredect - myture

t=0
idx = len(myerror)
for i in range(idx):
    if myerror[i]==0:
        t=t+1

tio = t/idx;
print(tio)








'''
import numpy as np
from sklearn.svm import SVC

file_path = r"/Users/xutingxi/Pyprojects/SelfProjects/mystudy/allnew.csv"
data = pd.read_csv(file_path)



mycolumns = [6,14,16,18,20,22,24,26,28,74,98,118,120,122]
all_train_data = data.iloc[:,mycolumns]
myindex =36000
table = all_train_data.iloc[2:myindex,:]
table = np.array(table)

myscore = data.iloc[2:myindex,126]
myscore = np.array(myscore)

clf = SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
      decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
       max_iter=-1, probability=False, random_state=None, shrinking=True,
      tol=0.001, verbose=False)
clf.fit(table, myscore) #doctest: +NORMALIZE_WHITESPACE
#print(clf.predict([[0.8,0.449,0.8,0.8,0.8,0.8,0.8,0.8,0.449,0.8,0.8,0.8,0.8,0.8]]))

all_test_data = data.iloc[:,mycolumns]

test = all_test_data.iloc[myindex:,:]
test = np.array(test)

myture = data.iloc[myindex:,126]
myture = np.array(myture)

mypredect = clf.predict(test)

myerror = mypredect - myture

t=0
idx = len(myerror)
for i in range(idx):
    if myerror[i]==0:
        t=t+1

tio = t/idx;
print(tio)



import xgboost as xgb
import numpy as np
file_path = r"/Users/xutingxi/Pyprojects/SelfProjects/mystudy/allnew.csv"
data = pd.read_csv(file_path)

mycolumns = [6,14,16,18,20,22,24,26,28,74,98,118,120,122]
all_train_data = data.iloc[:,mycolumns]
myindex =42000
table = all_train_data.iloc[2:myindex,:]
table = np.array(table)

myscore = data.iloc[2:myindex,126]
myscore = np.array(myscore)

dtrain = xgb.DMatrix(table, label=myscore)
num_round = 250
params = {
    'booster': 'gbtree',
    'num_class' :5,
    'eta': 0.1,
    'max_depth': 5,
    'min_child_weight': 1,
    'gamma': 0.0,
    'silent': 1,
    }
bst = xgb.train(params, dtrain, num_round)

all_test_data = data.iloc[:,mycolumns]

test = all_test_data.iloc[myindex:,:]
test = np.array(test)

dtest = xgb.DMatrix(test)
mypredect = bst.predict(dtest)

myture = data.iloc[myindex:,126]
myture = np.array(myture)
myerror = mypredect - myture


t=0
idx = len(myerror)
for i in range(idx):
    if myerror[i]==0:
        t=t+1

tio = t/idx;
print(tio)

'''
