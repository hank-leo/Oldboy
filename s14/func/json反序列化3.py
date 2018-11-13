#！/usr/bin/env python
# Author:Hank

import json
# import pickle

def sayhi(name):
    print("hello2,",name)

f=open('test.test','r')

# data=pickle.loads(f.read())
# data=pickle.load(f)
data=json.load(f)

# f.close()

print(data)

f.close()
