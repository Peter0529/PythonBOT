
import threading
import time
import api
# from actions.login import LogIn
from mychrome import MyChrome

class MyThread (threading.Thread):
  
    def __init__(self,settings):
        threading.Thread.__init__(self)

        self.is_working = True
        self.is_signed  = False

        # Set Bot Thread Settings

        # settings = {
        #     'MAX_ACTIVE_THREAD'             : MAX_ACTIVE_THREAD,
        #     'ERROR_LIMIT_PER_THREAD'        : ERROR_LIMIT_PER_THREAD,
        #     'TIMEOUT'                       : TIMEOUT,
        #     'PROXY_NOTE'                    : PROXY_NOTE,
        #     'CAMPAIGN_NOTE'                 : CAMPAIGN_NOTE,
        #     'MAX_MIXED'                     : MAX_MIXED,
        #     'MAX_PLAYS'                     : MAX_PLAYS
        # }

        self.settings = settings

        # get info from crud api response

        # sample of infos json structure

        # {'email_id': 4035, 'proxy': '192.126.209.165:8800', 'password': 'qkbpuTA=#33', 
        # 'agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36', 
        # 'agent_id': 615, 'connection': 'HTTP', 'proxy_id': 8123, 'type': 'PRIVATE', 'email': 'andrew.giuliano0187@cartone.life'}

        self.infos = api.getInfos(settings['PROXY_NOTE'])


        # Initialize Web Driver with Extensions
        self.webdriver = MyChrome(self.infos['proxy'],self.infos['agent'])
    
    def run(self):
        print
    
    def stop(self):
        self.webdriver.quit()
    