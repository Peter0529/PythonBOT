# -*- coding: utf-8 -*-

# API Integration Part with CRUD Server

from settings.main_settings import *
from http import HTTPStatus
import requests
import time
import urllib3
import json
import socket



# Disable Insecure Request Warning to HTTPS
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set Request Authorization Header
def sendGetRequest(url):
    return requests.get(url,auth=(CRUDAPI_USERNAME, CRUDAPI_PASSWORD),verify=False)

"""
Send POST request

...
Parameters
-----------
url     :  POST URL
data    :  POST Body Data

Response
-----------
return response of request

"""
def sendPostRequest(url,data):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    return requests.post(url,auth=(CRUDAPI_USERNAME, CRUDAPI_PASSWORD),data=json.dumps(data),verify=False,headers=headers)


#####################################################################################################
#                                                                                                   #
#                                         GET REQUEST                                               #
#                                                                                                   #
#####################################################################################################

"""
Get Bot Infos for Start Thread from CRUD

...
Parameters
-----------
proxy_note   :  Note for Filter Proxy

Response
-----------
return json of infos

sample of result

{'email_id': 4035, 'proxy': '192.126.209.165:8800', 'password': 'qkbpuTA=#33', 
'agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36', 
'agent_id': 615, 'connection': 'HTTP', 'proxy_id': 8123, 'type': 'PRIVATE', 'email': 'andrew.giuliano0187@cartone.life'}

"""
def getInfos(proxy_note):
    while True:
        # send request to crud server
        res = sendGetRequest(CRUDAPI_GET_INFOS + proxy_note)
        
        # if response is 200(ok) then exit while statement
        if(res.status_code == HTTPStatus.OK):
            break
        
        print("Failed get infos for starting bot! Retry after 30 seconds")

        # sleep for 30 sec and retry
        time.sleep(30)
    
    # Return json result
    return res.json()

"""
Get XPaths List from CRUD

...
Parameters
-----------

Response
-----------
return json of xpaths

sample of result

{'accept_button_before_signin':"//button[@class='qc-cmp-button'][text()=' I accept ']",'signin_button':"//a[@href='/login?redirectTo=%252F']",...}

"""
def getXPaths():
    # Send Get Request
    res = sendGetRequest(CRUDAPI_GET_S1_SETTINGS)

    # Check Response Status
    if(res.status_code != HTTPStatus.OK):
        print("Failed get XPaths info!")
    
    # Make Json Result from Response
    result = {}
    for i in range(1,26):
        value_index = "xpath{}".format(i)
        name_index  = value_index + "Desc"

        result[res.json()[name_index]] = res.json()[value_index]
    
    return result

# Global Variable XPaths
XPATHs = getXPaths()

#####################################################################################################
#                                                                                                   #
#                                         POST REQUEST                                              #
#                                                                                                   #
#####################################################################################################

"""
Send Error Log to CRUD Server

...
Parameters
-----------
xpath   :   Target Element
error   :   Error Text
proxy   :   Proxy
link    :   URL
campId  :   Campaign ID in CRUD DB

Response
-----------

"""

def sendErrorLog(xpath,error,proxy,link,campId):
    # Make body
    body = {}
    body['ip'] = socket.gethostbyname(socket.gethostname())
    body['campaign'] = "S1"
    body['xpath']    = xpath
    body['error']    = error
    body['link']     = link
    body['proxy']    = proxy
    body['campId']   = campId

    # Send POST request
    sendPostRequest(CRUDAPI_POST_ERROR_LOG,body)
