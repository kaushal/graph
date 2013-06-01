import numpy as np
import json
import urllib2
import simplejson
import matplotlib.pyplot as plt

data = urllib2.urlopen('http://contextminer.org/api.php/campaigns?u=chirags%40rutgers.edu&cid=516&source=youtube&everytime=1&ytid=wm4o1fYtCTQ&page=4&limit=25&fmt=json')


j = json.load(data)
print(j['data'][0])
viewcount = []
commentcount = []
favoritecount = []
x1 = []
x2 = []
x3 = []
count = 1
for video in j['data']: 
    viewcount.append(int(video['view_count']))
    commentcount.append(int(video['comment_count']))
    favoritecount.append(int(video['favorite_count']))
    x1.append(count - .3)
    x2.append(count)
    x3.append(count + .3)
    count = count + 1
print commentcount
print viewcount
print favoritecount
w = .3
ind = np.arange(5)
fig = plt.figure()
ax = fig.add_subplot(111)

ax.bar(x1, commentcount, width=w, color='b', align='center')
plt.savefig('coments.png')
ax.bar(x1, viewcount, width=w, color='g', align='center')
plt.savefig('views.png')
ax.bar(x1, favoritecount, width=w, color='r', align='center')
plt.show()
