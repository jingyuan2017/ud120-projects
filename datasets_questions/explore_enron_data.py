#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

import demjson

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

n=0
e=0
p=0
x=0
all=0

payment = 0
user = ""

for k,v in enron_data.items():
    
    all+=1
    #print k,len(v)

    if(k != "TOTAL" and v['total_payments'] != 'NaN' and v['total_payments'] > payment):
    	payment = v['total_payments'];
    	user = k;

    	print v;

    if(v['salary'] != 'NaN'):
    	print "salary"
    	n+=1

    if(v["email_address"] != 'NaN'):
    	e+=1

    if(v["total_payments"] == 'NaN'):
    	p+=1


    if(v['poi'] == True):
    	x+=1
    	#if(v["total_payments"] == 'NaN'):
    		#p+=1

print n;
print e;
print p;
print x;
print all;

print float(p)/x;

print(user);

print(payment);

#print enron_data[str.upper("SKILLING JEFFREY K")]


