import numpy as np
import json
import urllib2
import simplejson
import matplotlib.pyplot as plt

def graph(url):
    data = urllib2.urlopen(url)


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
    bx = fig.add_subplot(111)
    cx = fig.add_subplot(111) 

    ax.set_ylabel('Favorites Count')
    ax.set_xlabel('Time')
    ax.bar(x1, favoritecount, width=w, color='b', align='center')
    plt.savefig('favorites.png')
    ax.clear() 
     
    ax.set_ylabel('Comment Count')
    ax.set_xlabel('Time')
    ax.bar(x1, commentcount, width=w, color='g', align='center')
    plt.savefig('comments.png')
    ax.clear()

    ax.set_ylabel('View Count')
    ax.set_xlabel('Time')
    ax.bar(x2, viewcount, width=w, color='r', align='center')
    plt.savefig('views.png')
    ax.clear()

graph('http://contextminer.org/api.php/campaigns?u=chirags%40rutgers.edu&cid=516&source=youtube&everytime=1&ytid=wm4o1fYtCTQ&page=4&limit=25&fmt=json')
