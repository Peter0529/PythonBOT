from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from settings.main_settings import *
import random

class MyChrome(webdriver.Chrome):
    def __init__(self,proxy,agent):
        

        # Initialize Chrome Option
        options = ChromeOptions()

        # Set Chrome Options

        # add portable chrome path
        options.binary_location = PORTABLE_CHROME_PATH
        # add proxy
        options.add_argument('--proxy-server=http://%s' % proxy)
        # add user agent
        options.add_argument('--user-agent=%s' % agent)
        # add random window size
        options.add_argument('--window-size=%s' % WINDOW_SIZES[random.randint(0,len(WINDOW_SIZES) - 1)])
        # add random extensions

        for i in range(0,len(FORCE_EXTENSIONS_PATH) - 1):
            options.add_extension(FORCE_EXTENSIONS_PATH[i])
        
        for i in range(0,2):
            options.add_extension(RANDOM_EXTENSIONS_PATH[random.randint(0,len(RANDOM_EXTENSIONS_PATH) - 1)])
        
        super().__init__(executable_path=CHROME_DRIVER_PATH,chrome_options=options)

        



