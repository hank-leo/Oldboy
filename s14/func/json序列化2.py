#！/usr/bin/env python
# Author:Hank

# import json
import pickle

def sayhi(name):
    print('hello,',name)

info={
    'name':'hank',
    'age':25,
    'func':sayhi
}

f=open('test.test','wb')

# f.write(pickle.dumps(info))
pickle.dump(info,f)

f.close()

