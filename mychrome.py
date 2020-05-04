from selenium.webdriver.chrome.options import Options as ChromeOptions
from settings.main_settings import *
import random
import time
# import thread

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from api import *

class MyChrome(webdriver.Chrome):
    def __init__(self,proxy,agent,timeout):
        
        # Set Find Element Limit Time
        self.timeout = timeout

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
        
        super().__init__(executable_path=CHROME_DRIVER_PATH,options=options)




    
    ############### Customize Chrome Driver Methods ###############

    
    """
    navigateToUrl Function

    Navigate load completed page on chrome driver to url

    ...
    Parameters
    -----------
    url  : URL Link Text
    
    Response
    -----------
    True or False if success or fail

    """
    def navigateToUrl(self,url):
        try:
            # Go to Link
            self.get(url)
            # Wait for document is ready for complete
            return self.execute_script('return document.readyState;') == 'complete'
        except Exception as e:
            print(e)
            return False

    """
    typeTextandEnter Function

    Type text and press enter

    ...
    Parameters
    -----------
    xpath : Target Element XPATH
    text  : Input Text
    
    Response
    -----------
    True or False if success or fail

    """
    def typeTextandEnter(self,xpath,text):
        try:
            # Wait until target element is located and get the element
            element = WebDriverWait(self, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            # Type text in target element
            element.send_keys(text)
            # Press enter key
            element.send_keys(Keys.ENTER)
            return True
        except Exception as e:
            print(e)
            return False

    """
    checkIfElementIsDisplayed Function

    Check if the xpath element is displayed

    ...
    Parameters
    -----------
    xpath : Target Element XPath
    
    Response
    -----------
    True or False if success or fail

    """
    def checkIfElementIsDisplayed(self,xpath):
        try:
            # Wait until target element is displayed then return true
            if(WebDriverWait(self,self.timeout).until(EC.presence_of_element_located((By.XPATH,xpath))).is_displayed()):
                return True
        except Exception as e:
            print(e)
            return False

    """
    randomScrolling Function

    Random Scrolling on Current Page,Scroll less than 3 Times,Scroll Height = random(0,1000)

    ...
    Parameters
    -----------
    

    Response
    -----------
    True or False if success or fail

    """
    def randomScrolling(self):
        try:
            # Less than 3 times
            for i in random.randint(0,2):
                # Scroll between (0,1000)
                self.execute_script("window.scrollBy(0,{})".format(random.randint(0,999)))
                time.sleep(0.5)
            
            return True
        except Exception as e:
            print(e)
            return False
        
    """
    scrollToTop Function

    Scroll To Top of Page Function

    ...
    Parameters
    -----------
    
    
    Response
    -----------
    True or False if success or fail

    """
    def scrollToTop(self):
        self.execute_script("window.scrollTo(0,0)")
    
    """
    buttonClick Function

    Use this function when click special button has click event redirect to internal element
    ...
    Parameters
    -----------
    xpath : Target Element XPath
    
    Response
    -----------
    True or False if success or fail

    """
    def buttonClick(self,xpath):
        try:
            # Click Internal Element
            self.execute_script("arguments[0].click();",self.find_element_by_xpath(xpath))
            return True
        except Exception as e:
            print(e)
            return False
    
    """
    checkIfElementIsPresent Function

    ...
    Parameters
    -----------
    xpath : Target Element XPath
    
    Response
    -----------
    True or False if success or fail

    """
    def checkIfElementIsPresent(self,xpath):
        # Total try times
        times = 0
        while(times < 3):
            try:
                # Wait Until Target Element is Displayed and Click
                element = WebDriverWait(self,self.timeout).until(EC.element_to_be_clickable((By.XPATH,xpath)))
                if(element.is_displayed()):
                    return self.buttonClick(xpath)
            except Exception as e:
                print(e)
                pass
            
            # Increase Times
            times = times + 1

            # Not Found Until Retry 3 Times then Refresh Current Page
            if(times == 3):
                self.refresh()
            
        return False
    
    """
    showDotMenu Function

    Reup,Highlights functions should be check ... menu depending on window size.
    Click ... menu function before click buttons such as reup,highlights

    ...
    Parameters
    -----------
    
    Response
    -----------
    True or False if success or fail

    """

    def showDotMenu(self):
        try:
            # Go to Top of Current Page
            self.scrollToTop()
            # Click DotMenu Button
            self.find_element_by_xpath(XPATHs['show_dotmenu_button']).click()

            return True
        except Exception as e:
            print(e)
            return False
    
    """
    showStatusInBar Function

    Show Chrome Bar Status Info and Random Scrolling(Prefix:P,F,M)

    ...
    Parameters
    -----------
    prefix      : 'P'(play),'F'(follow),'M'(reup,highlight,favorite)
    min_time    : minimum seconds of playing
    max_time    : maximum seconds of playing
    nr_of_songs : number of songs count
    count       : played count
    max_count   : max played count
    
    Response
    -----------
    True or False if success or fail

    """

    def showStatusInBar(self,prefix,min_time,max_time,nr_of_songs,count,max_count):
        # Start Random Scroll with Thread
        thread.start_new_thread(self.randomScrolling)

        # Set play time to random between min and max time
        play_time = random.randint(min_time,max_time)

        try:
            for i in range(0,play_time):
                # Set Title
                title = "{}({}/{}):??({}/{})#{}".format(prefix,i,play_time,count,max_count,nr_of_songs)
                self.excute_script("document.title = '{}'".format(title))
                # Wait for one second
                time.sleep(1)
        except Exception as e:
            print(e)
            return False
        
        return True

    """
    playOneSong Function

    Play one song before Actions,Return error json object(xpath,error)

    ...
    Parameters
    -----------
    prefix      : 'P'(play),'F'(follow),'M'(reup,highlight,favorite)
    count       : played count
    max_count   : max played count
    
    Response
    -----------

    return error log if fail,none if success

    {xpath,error description}

    """
    def playOneSong(self,prefix,count,max_count):

        # Mixed(reup,highlight,favorite)
        if(prefix == 'M'):
            playbutton_xpath  = XPATHs['startplaysong_button_in_play_reup_highlight_favorite']
            pausebutton_xpath = XPATHs['playingnow_in_play_reup_highlight_favorite']
        # Follow
        elif(prefix == 'F'):
            playbutton_xpath  = XPATHs['startplayfirstsong_button_in_follow']
            pausebutton_xpath = XPATHs['playingnow_in_follow']
        
        try:
            # Click play button
            self.buttonClick(playbutton_xpath)
            # Check playing and show status in chrome bar
            if(self.checkIfElementIsDisplayed(pausebutton_xpath)):
                # Show status bar 90-150 sec,one song
                self.showStatusInBar(prefix,90,150,1,count,max_count)
                return None
            else:
                # Return json error log
                return {pausebutton_xpath,"Not found playingnow after click startplaybutton in mixed action"}
        except Exception as e:
            print(e)
            return {playbutton_xpath,"Not found startplaysong button before do mixed action"}
    
    """
    isPageLoadSuccess Function

    check current page loaded successfully

    ...
    Parameters
    -----------
    
    Response
    -----------
    return True if present,False if not present

    """

    def isPageLoadSuccess(self):
        try:
            # get target element that class name is 'error-code'
            element = self.find_element_by_class_name('error-code')
            # check target element text is in page error list
            if(element.text in PAGE_ERR_STR_LIST):
                return False
            else:
                return True
        
        # if not found target element then...
        except NoSuchElementException as e:
            print("page loaded successfully")
            return True
    
    """
    isAcceptButtonPresent Function

    check accept cookies button appear when try to login
    if the element present then click
    ...
    Parameters
    -----------
    
    Response
    -----------
    return True if present,False if not present

    """

    def isAcceptButtonPresent(self):
        # wait 2 seconds because this button appear in 2 seconds after main website page loaded
        time.sleep(2)
        try:
            # find target element by xpath
            element = self.find_element_by_xpath(XPATHs['accept_button_before_signin'])
            # click target element
            element.click()
            return True
        except NoSuchElementException as e:
            print("not found accept-button when signin")
            return False