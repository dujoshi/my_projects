import requests
import json
import os
import sys, time, pdb
import json

def post2(apic_ip):
     login_url = "https://{}/api/aaaLogin.json".format(apic_ip)
     data = {"aaaUser":{"attributes":{"name": "admin", "pwd": "ins3965!"}}}
     headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

     r = requests.post(login_url, data=json.dumps(data), headers=headers, verify=False)
     cookie=r.cookies.get_dict()

     post_url="https://{}/api/node/mo/uni/tn-T0/ap-A0/epg-EPG11.json".format(apic_ip)
     payload = {"fvRsDomAtt":{"attributes":{"resImedcy":"pre-provision","tDn":"uni/vmmp-VMware/dom-DVS2","status":"deleted"},"children":[{"vmmSecP":{"attributes":{"status":"deleted"},"children":[]}}]}}

     headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'} # set what your server accepts
     r = requests.post(post_url, data=json.dumps(payload), headers=headers,verify=False, cookies=cookie)
     print r

APIC_IP="x.x.x.x"     
post2(APIC_IP)

"""
1- In cisco Apic we have a API Inspector which if you turn on and try doing any configuration via GUI
    it'll provide you exact json related to hat object.
2- you can just put that json in payload and one the authentication is done, use the same cookies and 
   perform the action.
3- In above code we are first doing the authentication and once the authentication is done we are using the cookies 
   and posting the congiration to APIC.
   
"""
