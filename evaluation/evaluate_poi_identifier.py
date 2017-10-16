#!/usr/bin/python
# coding=utf-8 

"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import train_test_split

feature_train , feature_test , label_train , label_test = train_test_split(features , labels , test_size = 0.3 , random_state = 42);

clf = DecisionTreeClassifier(random_state=0);

clf.fit(feature_train , label_train);

print clf.score(feature_test , label_test);

print type(label_test);

print len(label_test)

print list(filter(lambda x: x > 0, label_test))


#输出真实数据和预测数据
print label_test;

pred = clf.predict(feature_test);

print pred;


from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

#输出准确率
print precision_score(label_test , pred)

#输出召回率
print recall_score(label_test , pred)



#输出值
p = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
#真实值
t = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

#真正例输出
n=0;
for i in range(0,len(t)):
	if(t[i] == 1 and p[i] == 1):
		n+=1
print "真正例" + str(n);


#真负例输出
n=0;
for i in range(0,len(t)):
	if(t[i] == 0 and p[i] == 0):
		n+=1
print "真负例" + str(n);

#假正例输出
n=0;
for i in range(0,len(t)):
	if(t[i] == 0 and p[i] == 1):
		n+=1
print "假正例" + str(n);


#假负例输出
n=0;
for i in range(0,len(t)):
	if(t[i] == 1 and p[i] == 0):
		n+=1
print "假负例" + str(n);
