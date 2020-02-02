#for Duo we can download the package from DUO URLs
# and here is the sample code i used to get the bypass code for a user
# DUO APIs: https://github.com/duosecurity?utf8=%E2%9C%93&q=python&type=&language=


#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import print_function
import csv, pdb
import sys

import duo_client
from six.moves import input

argv_iter = iter(sys.argv[1:])
def get_next_arg(prompt):
    try:
        return next(argv_iter)
    except StopIteration:
        return input(prompt)

# Configuration and information about objects to create.
admin_api = duo_client.Admin(
    ikey=XXXXX,
    skey=XXXXX,
    host='XXXXX',
)

# Retrieve user info from API:

users = admin_api.get_users()
try:
      for user_info in users:
           if user_info['username']=='duo_automation_user':
                print (user_info['user_id'])
                user_id= user_info['user_id']
except:
     print ("exception ")


bypass_code=admin_api.add_user_bypass_codes(user_id)
print (bypass_code)

'''
Output: 
It'll give you a list of 10 Bypass codes. 
[dujoshi@DUJOSHI-M-K1YF:~] $ python get_pass_code.py
DUOJAV04FI3QCONWMPOI
[u'115784836', u'809973997', u'467969983', u'036840251', u'677877803', u'877451622', u'892989534', u'657567549', u'966076702', u'983695711']
[dujoshi@DUJOSHI-M-K1YF:~] $
'''
