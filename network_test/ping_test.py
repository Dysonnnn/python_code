########!/usr/bin/python
# -*- coding:utf8 -*-
"""Document: network script, keep network always working, using python3"""
import os
import time
PING_RESULT = 0
NETWORK_RESULT = 0
def DisableNetwork():
 ''' disable network card '''
 result = os.system(u"netsh interface set interface 以太网 disable")
 if result == 1:
  print("disable network card failed")
 else:
  print("disable network card successfully")
def ping():
 ''' ping 主备网络 '''
 #result = os.system(u"ping 180.97.33.108")
 result = os.system(u"ping www.baidu.com -l 1472 -n 100")
 if result == 0:
  print("A网正常")
 else:
  print("网络故障")
 return result
if __name__ == '__main__':
 while True:
  PING_RESULT = ping()
  if PING_RESULT == 0:
   time.sleep(20)
  else:
   DisableNetwork()
   time.sleep(10)