
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Login():
  def start():
    self.driver = webdriver.Chrome(executable_path=r'pytest/chromedriver.exe')
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    # Test name: login
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://audiomack.com/")
    # 2 | setWindowSize | 1038x742 | 
    self.driver.set_window_size(1038, 742)
    # 3 | waitForElementPresent | xpath=//a[contains(text(),'Sign in')] | 30000
    WebDriverWait(self.driver, 30000).until(expected_conditions.presence_of_element_located((By.XPATH, "//a[contains(text(),\'Sign in\')]")))
    # 4 | click | xpath=//a[contains(text(),'Sign in')] | 
    self.driver.find_element(By.XPATH, "//a[contains(text(),\'Sign in\')]").click()
    # 5 | waitForElementPresent | xpath=//input[@name='email'] | 30000
    WebDriverWait(self.driver, 30000).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@name=\'email\']")))
    # 6 | type | xpath=//input[@name='email'] | robert.campbell4681@cartone.life
    self.driver.find_element(By.XPATH, "//input[@name=\'email\']").send_keys("robert.campbell4681@cartone.life")
    # 7 | click | xpath=(//button[@type='submit'])[2] | 
    self.driver.find_element(By.XPATH, "(//button[@type=\'submit\'])[2]").click()
    # 8 | waitForElementPresent | xpath=//input[@id='password'] | 30000
    WebDriverWait(self.driver, 30000).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@id=\'password\']")))
    # 9 | click | xpath=//input[@id='password'] | 
    self.driver.find_element(By.XPATH, "//input[@id=\'password\']").click()
    # 10 | type | xpath=//input[@id='password'] | wibthBB=(07
    self.driver.find_element(By.XPATH, "//input[@id=\'password\']").send_keys("wibthBB=(07")
    # 11 | click | xpath=(//button[@type='submit'])[2] | 
    self.driver.find_element(By.XPATH, "(//button[@type=\'submit\'])[2]").click()
    # 12 | waitForElementPresent | xpath=//button/div/span | 30000
    WebDriverWait(self.driver, 30000).until(expected_conditions.presence_of_element_located((By.XPATH, "//button/div/span")))