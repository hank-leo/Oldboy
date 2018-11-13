#！/usr/bin/env python
# Author:Hank

#语法糖

import time

user,passwd='hank','123'
def auth(auth_type):
    print('auth func:',auth_type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            print('wrapper func args:',*args, **kwargs)
            if auth_type == 'local':
                username = input('Username:').strip()
                password = input('Password:').strip()
                if user == username and passwd == password:
                    print('\033[32;1mUser has passed authentication\033[0m')
                    res = func(*args, **kwargs)  # from home
                    print('---after authenticaion')
                else:
                    exit('\033[31;1mInvalid has passed authentication\033[0m')
            elif auth_type == 'ldap':
                print('不会ldap...')

        return wrapper
    return outer_wrapper

def index():
    print('welcome to index page')

@auth(auth_type="local")
def home():
    print('welcome to home page')
    return 'from home'

@auth(auth_type="ldap")
def bbs():
    print('welcome to bbs page')

index()
print(home())
bbs()