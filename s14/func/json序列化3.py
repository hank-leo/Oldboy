#！/usr/bin/env python
# Author:Hank

import json
# import pickle

def sayhi(name):
    print('hello,',name)

info={
    'name':'hank',
    'age':25,
    # 'func':sayhi
}

f=open('test.test','w')
f.write(json.dumps(info))
# f.write(pickle.dumps(info))
# json.dump(info,f)

info['age'] = 21



f.close()

