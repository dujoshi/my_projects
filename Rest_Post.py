import requests
import json
import os
import sys, time, pdb

def post():
     login_url = "https://x.x.x.x/api/aaaLogin.json"
     data = {"aaaUser":{"attributes":{"name": "admin", "pwd": "XYZPASSWORD"}}}
     headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

     r = requests.post(login_url, data=json.dumps(data), headers=headers, verify=False)
     #Here we are taking the cookie for this authentication session with us. 
     #This will use for further requests.  
     cookie=r.cookies.get_dict()
     
     
     post_url="https://x.x.x.x/api/node/mo/uni.xml"
     #Below post will create an EPG on APIC ACI
     xml_data = """
<?xml version="1.0" encoding="UTF-8"?><imdata totalCount="1"><fvAEPg annotation="" descr="" dn="uni/tn-T1/ap-AP1/epg-Test" exceptionTag="" floodOnEncap="disabled" fwdCtrl="" hasMcastSource="no" isAttrBasedEPg="no" matchT="AtleastOne" name="Test" nameAlias="" pcEnfPref="unenforced" prefGrMemb="exclude" prio="unspecified" shutdown="no"/></imdata>
        """

     headers = {'Content-Type': 'application/xml'} # set what your server accepts
     #See below we are using cookie which we got during authentication
     rr = requests.post(post_url, data=xml_data, headers=headers, verify=False, cookies=cookie)
     pdb.set_trace()
     print rr

print "\n ========================== \n"
print "\n Createing EPG"
print "\n ========================== \n"

post()
