from numpy import spacing
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

path = ChromeDriverManager().install()
driver = webdriver.Chrome(path)
n = input()
from time import sleep
sleep(10)
driver.get("http://www.google.com")
qt = driver.find_element("xpath", "//input[@name='q']")
qt.send_keys(str(n))
qt.send_keys(Keys.RETURN)
sleep(10)