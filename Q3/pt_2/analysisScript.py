'''
This script extracts string length of each post, score of each post and number of views of each post
and stores the database in json format
'''


from lxml import etree
import matplotlib.pyplot as plt
import json


masterList = []
class TitleTarget(object):
    def __init__(self):
        self.text = []
        self.x = 0
    def addAttr(self,score,view,body):
        masterList.append({'score':score, 'view':view, 'length':body})
    
    def start(self, tag, attrib):
        # if '"Tags"' in attrib.keys():
            # print(attrib['Tags'])
        # print(self.x)
        # self.x+=1
        if tag == 'row' and 'Score' in attrib.keys() and 'ViewCount' in attrib.keys() and 'Body' in attrib.keys():
            self.addAttr(attrib['Score'],attrib['ViewCount'],len(attrib['Body']))
        self.is_tag = True if tag == 'Title' else False
    def end(self, tag):
        pass
        # if tag not in masterList:
        #     masterList.append(tag)
    def data(self, data):
        if self.is_tag:
            print(data.encode('utf-8'))
    def close(self):
        return self.text
 
 
 
parser = etree.XMLParser(target = TitleTarget())
infile = './Posts.xml'
results = etree.parse(infile, parser)    

with open("extemp.json", "w") as outfile:  
    json.dump(masterList, outfile) 
# plt.bar(masterList.keys(),masterList.values(),color='g')


# X = [] #  length
# Y = [] #  view
# Z = [] #  body

# for i in masterList:
#     X.append(i['length'])
#     Y.append(i['view'])
#     Z.append(i['score'])

# plt.scatter(X,Y,s=0.5,color='g')
# plt.show()