import time
import re
import os, sys, traceback
import tempfile, pdb
import threading, logging
import pdb
import pexpect
import paramiko
import requests
from com.vmware import nsx_client
from com.vmware import nsx_policy_client
from vmware.vapi.bindings.stub import ApiClient
from vmware.vapi.bindings.stub import StubFactory
from vmware.vapi.lib import connect
from vmware.vapi.security.user_password import \
    create_user_password_security_context
from vmware.vapi.stdlib.client.factories import StubConfigurationFactory

from vmware.vapi.bindings.struct import PrettyPrinter
from com.vmware.nsx.model_client import TransportZone
from com.vmware.vapi.std.errors_client import NotFound

BASIC_AUTH = 1
SESSION_AUTH = 2


class NSXT():
	def __init__(self, ip, username='admin', password="Ciscoins3965!", tcp_port=443, auth_type=SESSION_AUTH, logger=None):
	    self.ip = ip
	    self.username = username
	    self.password = password
            self.tcp_port=tcp_port
            self.auth_type= auth_type
	    self.clientdict = {}
	    self.logger = logger

	def log_line(self, line):
	    if self.logger == None:
		 print line
	    else:
		 self.logger.info(line)


	def get_basic_auth_stub_config(self):
	    """
	    Create a stub configuration that uses HTTP basic authentication.
	    """
	    session = requests.session()

	    # Since the NSX manager default certificate is self-signed,
	    # we disable verification. This is dangerous and real code
	    # should verify that it is talking to a valid server.
	    session.verify = False
	    requests.packages.urllib3.disable_warnings()

	    nsx_url = 'https://%s:%s' % (self.ip, self.tcp_port)
	    connector = connect.get_requests_connector(
		session=session, msg_protocol='rest', url=nsx_url)
	    stub_config = StubConfigurationFactory.new_runtime_configuration(
		connector, response_extractor=True)
	    security_context = create_user_password_security_context(
		self.username, self.password)
	    connector.set_security_context(security_context)
	    return stub_config


	def get_session_auth_stub_config(self):
	    """
	    Create a stub configuration that uses session-based authentication.
	    Session authentication is more efficient, since the server only
	    needs to perform authentication of the username/password one time.
	    """
	    session = requests.session()

	    # Since the NSX manager default certificate is self-signed,
	    # we disable verification. This is dangerous and real code
	    # should verify that it is talking to a valid server.
	    session.verify = False
	    requests.packages.urllib3.disable_warnings()
	    nsx_url = 'https://%s:%s' % (self.ip, self.tcp_port)
	    resp = session.post(nsx_url + "/api/session/create",
				data={"j_username": self.username, "j_password": self.password})
	    if resp.status_code != requests.codes.ok:
		resp.raise_for_status()

	    # Set the Cookie and X-XSRF-TOKEN headers
	    session.headers["Cookie"] = resp.headers.get("Set-Cookie")
	    session.headers["X-XSRF-TOKEN"] = resp.headers.get("X-XSRF-TOKEN")

	    connector = connect.get_requests_connector(
		session=session, msg_protocol='rest', url=nsx_url)
	    stub_config = StubConfigurationFactory.new_runtime_configuration(
		connector, response_extractor=True)
	    return stub_config


	def get_session_auth_api_client(self):
	    stub_config = get_session_auth_stub_config(self,
		self.username, self.password, self.ip, self.tcp_port)
	    stub_factory = nsx_client.StubFactory(stub_config)
	    return ApiClient(stub_factory)


	def create_api_client(self, auth_type=BASIC_AUTH,):
	    if auth_type == BASIC_AUTH:
		stub_config = self.get_basic_auth_stub_config()
	    elif auth_type == SESSION_AUTH:
		stub_config = get_session_auth_stub_config(self)
	    stub_factory = nsx_client.StubFactory(stub_config)
	    return ApiClient(stub_factory)

	def create_nsx_policy_api_client(self, auth_type=BASIC_AUTH,):
	    if auth_type == BASIC_AUTH:
		stub_config = self.get_basic_auth_stub_config()
	    elif auth_type == SESSION_AUTH:
		stub_config = get_session_auth_stub_config(self)
	    stub_factory = nsx_policy_client.StubFactory(stub_config)
	    return ApiClient(stub_factory)
        
        # FROM HERE OUR CODE FOR DIFF ACI INTEGRATION AND CHECK ON NSX_MANAGER STARTS
     
        def Get_Transport_Zone(self):
            """
            This Function will return a list of all transportzone
            details available on NSX manager with full data. 
            return: if all good : list of NSX Transport Zones
                    else: False
            """ 
            try: 
               client=self.create_api_client()
               pp = PrettyPrinter()
               tzs = client.TransportZones.list()
               return tzs
            except:  
               self.log_line(traceback.format_exc()) 
               return False

        def Find_Transport_Zone(self,tzone_name):
            """
            We will take the NSXT Handle and verify if TransportZone
            given in the args exist on NSXT or not:    
            input args: tzone_nameA
            return :  True/False  based on Availability 
            """
            try: 
               client=self.create_api_client()
               pp = PrettyPrinter()
               tzs = client.TransportZones.list()
               if tzs:
                  tzs_list=map(lambda x:x.display_name, tzs.results) 

               self.log_line("\n List Of Available TransportZone:  {}".format(tzs_list))
               if tzone_name in tzs_list: 
                  return True
               else:
                  return False 
            except:  
               self.log_line(traceback.format_exc()) 
               return False


        def Find_Transport_Zone(self,tzone_name,description="APIC created TZ", traffic_type='VLAN'):
            """
            We will take the NSXT Handle and verify if TransportZone
            given in the args exist on NSXT or not:    
            input args: tzone_nameA
            return :  True/False  based on Availability 
            """
            try: 
               client=self.create_api_client()
               pp = PrettyPrinter()
               tzs = client.TransportZones.list()
               pdb.set_trace()
               for tz in tzs.results: 
                   if tz.display_name == tzone_name:  
                      if tz.description != description: 
                         self.log_line("\nTransport zone expected: {} Found : {}".format(description,tz.description))
                         return False
                      if tz.transport_type != traffic_type:
                         self.log_line("\nTransport zone Transport expected: {} Found : {}".format(traffic_type, tz.transport_type))
                         return False

                      self.log_line("\nTransport zone available on NSX-T Manager as Expected ")
                      return True  
               return False 
            except:  
               self.log_line(traceback.format_exc()) 
               return False
