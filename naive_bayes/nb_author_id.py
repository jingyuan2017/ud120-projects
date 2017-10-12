#!/usr/bin/python
#coding=utf-8

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import time


print "预处理数据"

timeStartX = time.time();

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()



#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 


#########################################################
### your code goes here ###


#########################################################

timeStart = time.time();
print "预处理耗时 : " + str(round((timeStart - timeStartX),3))


print "开始训练"

#clf = GaussianNB();
clf = SVC(kernel='rbf' , C=10000)

clf.fit(features_train,labels_train);

timeFit = time.time();

print "训练耗时 : " + str(round((timeFit - timeStart),3))

result = clf.predict(features_test);

timePred = time.time();
print "预测耗时 : " + str(round((timePred - timeFit),3))

print(result);

print (result > -1).sum()
print (result == 0).sum()
print (result == 1).sum()

score = clf.score(features_test , labels_test);

print("预测准确率:" + str(score))
