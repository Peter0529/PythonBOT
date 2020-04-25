# -*- coding: utf-8 -*-

# API Integration Part with CRUD Server

from settings.main_settings import *
from http import HTTPStatus
import requests
import time
import urllib3

# Disable Insecure Request Warning to HTTPS
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set Request Authorization Header
def sendGetRequest(url):
    return requests.get(url,auth=(CRUDAPI_USERNAME, CRUDAPI_PASSWORD),verify=False)

def sendPostRequest(url):
    return requests.post(url,auth=(CRUDAPI_USERNAME, CRUDAPI_PASSWORD),verify=False)

# Get Bot Infos for Start Thread from CRUD
def getInfos(proxy_note):
    while True:
        # send request to crud server
        res = sendGetRequest(CRUDAPI_GET_INFOS + proxy_note)
        
        # if response is 200(ok) then exit while statement
        if(res.status_code == HTTPStatus.OK):
            break
        
        # sleep for 30 sec and retry
        time.sleep(30)
    
    return res.json()


    

