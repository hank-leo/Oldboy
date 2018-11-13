#！/usr/bin/env python
# Author:Hank

import time

x=time.localtime()
# print(x)

time.strftime("%m:%d %H:%M:%S %Y",x)