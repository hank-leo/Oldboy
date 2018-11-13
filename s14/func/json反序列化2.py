#！/usr/bin/env python
# Author:Hank

# import json

import pickle
def sayhi(name):
    print("hello2,",name)

f=open('test.test','rb')

# data=pickle.loads(f.read())
data=pickle.load(f)

# f.close()

print(data['func','hank'])
