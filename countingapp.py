import os.path
import re
fname = 'testing.txt'
a = os.path.isfile(fname)
if a == True:
    while True:
        hashtag = raw_input('Please type in a hashtag; when done please type done: ')
        if hashtag == 'done':
            break
        website = raw_input('Please type in website found; when done please type done.\
        \nenter 1:hashtagify.me,\n 2:hashtags.org,\n 3:keyhole.co,\n 4:ritetag.com\
        \n 5. quora.com: ')
        d = hashtag+","+website
        if website =='done':
            break
        else:
            with open(fname,'a') as file_object:
                file_object.write(d+"\n")
            continue
else:
    while True:
        hashtag = raw_input('Please type in a hashtag; when done please type done: ')
        if hashtag == 'done':
            break
        website = raw_input('Please type in website found; when done please type done.\
        \nenter 1:hashtagify.me,\n 2:hashtags.org,\n 3:keyhole.co,\n 4:ritetag.com\
        \n 5. quora.com: ')
        d = hashtag+","+website
        if website =='done':
            break
        else:
            with open(fname,'w') as file_object:
                file_object.write(d+"\n")
            break
    while True:
        hashtag = raw_input('Please type in a hashtag; when done please type done: ')
        if hashtag == 'done':
            break
        website = raw_input('Please type in website found; when done please type done.\
        \nenter 1:hashtagify.me,\n 2:hashtags.org,\n 3:keyhold.co,\n 4:ritetag.com,\
        \n 5. quora.com: ')
        d = hashtag+","+website
        if website =='done':
            break
        else:
            with open(fname,'a') as file_object:
                file_object.write(d+"\n")
            continue

with open(fname) as file_object:
    contents = file_object.readlines()
number = 0
for line in contents:
    sameline = line.rstrip()
    number += 1
    #print str(number)+".",sameline

def hashx(object,object1):
    z = object.split(',')
    hashname = z[0].lower()
    if z[1] == '1':
        z[1] = 'hashtagify.me'
    elif z[1] == '2':
        z[1] = 'hashtags.org'
    elif z[1] == '3':
        z[1] = 'keyhole.co'
    elif z[1] == '4':
        z[1] = 'ritetag.com'
    elif z[1] == '5':
        z[1] = 'quora.com'
    website = z[1]
    if hashname in object1.keys():
        temp = list()
        temp.append(website)
        object1[hashname]=object1[hashname]+temp
    else:
        temp = list()
        temp.append(website)
        object1[hashname]=temp
hashdict=dict()
for line in contents:
    just = line.rstrip()
    hashx(just,hashdict)
#for hash, websites in hashdict.items():
    #print hash, websites

hashlist=list()
for hash, websites in hashdict.items():
    hashlist.append((len(websites),hash))
hashlist.sort(reverse = True)
rank = 0
for noweb, hash in hashlist [0:10]:
    rank += 1
    print str(rank)+'.', hash, noweb
