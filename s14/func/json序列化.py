#！/usr/bin/env python
# Author:Hank

# import json
# import pickle

# def sayhi(name):
#     print('hello,',name)

# info={
#     'name':'hank',
#     'age':25,
#     'func':sayhi
# }

# f=open('test.test','wb')

# print(json.dumps(info))

# f.write(json.dumps(info))

# f.write(pickle.dumps(info))
# f.write(pickle.dump(info))

# f.close()

# eval()



#import json

import pickle

def sayhi(name):
    print("hello,",name)

info = {
    'name':'alex',
    'age':22,
    'func':sayhi
}

f = open("test.text","wb")

pickle.dump(info,f) #f.write( pickle.dumps( info) )

f.close()
