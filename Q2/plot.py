import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import tweepy
import sys
import re
import string
import preprocessor as p
import math

# mu = 200
# sigma = 25
# n_bins = 100
Dictionary = []
fn = input('Enter filename : ')
# fileData = open(fn, 'r')
counter = 0
with open(fn, 'r') as data:
    for line in csv.DictReader(data):
        line['username'] = line['username'].split('b\'')[-1]
        Dictionary.append(line)

print('total data', len(Dictionary))


# Language analysis
lang = {}
L_no = []
L_names = []
L_color = []
for i in Dictionary:
    if i['lang'] not in lang:
        lang[i['lang']] = 0
    lang[i['lang']] += 1
print('Language Analysis of tweets')
col = ['red', 'green', 'blue', 'cyan', 'orange', 'brown', 'pink']
ind = 0
for i in lang.keys():
    L_names.append(i)
    L_no.append(lang[i])
    L_color.append(col[ind % 7])
    ind += 1

plt.pie(L_no,labels=L_names,colors=L_color)
plt.axis('equal')
plt.show()


print(lang)


# Follower / Following Analysis
FF_data = {}
for i in Dictionary:
    print(i['username'])
    FF_data[i['username']] = {'following': i['following'],
                              'followers': i['followers'], 'likes': i['likes'], 'retweets': i['retweets']}

print("Follow Data")
trendData = []
for i in FF_data.keys():
    if int(FF_data[i]['retweets']) == 0:
        trendData.append(FF_data[i]['followers'])
    else:
        trendData.append(float(FF_data[i]['followers'])/float(FF_data[i]['retweets']))


plt.hist(trendData,color='g',cumulative=True,rwidth=10)
plt.show()
# print(sorted(trendData))

# time analysis
# number of tweets per 5 mins time interval
X = []
freq = []
timeDict = {}
for i in Dictionary:
    tempList = re.split(' |-|:',i['timestamp'])
    for i in range(len(tempList)): 
        tempList[i] = int(tempList[i])
    key = int(math.floor(tempList[-2]/5)+100*tempList[-3]+10000*tempList[-4])
    # print(key)
    if key not in timeDict:
        timeDict[key] = 0
    timeDict[key] += 1

z = 0
for i in timeDict.keys():
    X.append(z)
    freq.append(timeDict[i])
    z+=1

plt.plot(X,freq)
plt.show()
    