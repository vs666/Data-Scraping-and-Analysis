import matplotlib.pyplot as plt
import json 

f = open('sample.json')
data = json.load(f)
dis = {}
data = sorted(data.items(), key=lambda x:x[1],reverse=True)
for i in range(10):
    dis[data[i][0]]=data[i][1]

plt.bar(dis.keys(),dis.values(),color='g')
plt.show()
