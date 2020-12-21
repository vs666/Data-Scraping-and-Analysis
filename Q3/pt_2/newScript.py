from lxml import etree
import matplotlib.pyplot as plt
import json


masterList = {}
class TitleTarget(object):
    def __init__(self):
        self.text = []
        self.x = 0
    def addAttr(self,s):
        stmp = ''
        for c in s:
            if c == '<':
                continue
            elif c=='>':
                if stmp not in masterList.keys():
                    masterList[stmp] = 0
                masterList[stmp]+=1
                stmp=''
            else:
                stmp+=c
        
    def start(self, tag, attrib):
        # if '"Tags"' in attrib.keys():
            # print(attrib['Tags'])
        # self.x+=1
        if tag == 'row' and 'Tags' in attrib.keys():
            self.addAttr(attrib['Tags'])
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
 
out = open('titles.txt', 'w')
out.write('\n'.join(results))
out.close()

with open("sample.json", "w") as outfile:  
    json.dump(masterList, outfile) 
plt.bar(masterList.keys(),masterList.values(),color='g')