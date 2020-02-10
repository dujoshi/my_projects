import requests
import json
import os
import sys, time, pdb

def post():
     login_url = "https://x.x.x.x/api/aaaLogin.json"
     data = {"aaaUser":{"attributes":{"name": "admin", "pwd": "ins3965!"}}}
     headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

     r = requests.post(login_url, data=json.dumps(data), headers=headers, verify=False)
     cookie=r.cookies.get_dict()
     post_url="https://x.x.x.x/api/node/mo/uni.xml"

     xml_data = """
<?xml version="1.0" encoding="UTF-8"?><imdata totalCount="1"><pcAggrIf adminSt="down"
  dn="topology/pod-1/node-101/sys/aggr-[po2]"
 id="po2"/></imdata>
     """

     headers = {'Content-Type': 'application/xml'} # set what your server accepts
     rr = requests.post(post_url, data=xml_data, headers=headers, verify=False, cookies=cookie)
     pdb.set_trace()
     print rr

post()


"""
Above code is again the same kind of example using xml how we can do a post on APIC. 
we are first doing authentication and than using the same cookie and posting the relevent configuration 
to apic Server
"""
