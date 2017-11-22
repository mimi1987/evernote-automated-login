#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


#CREATE DRIVER

driver = webdriver.Firefox()


#OPEN URL

driver.get('https://www.evernote.com/Login.action')


#LOGIN PROCESS

elem_username = driver.find_element_by_name('username')
elem_username.send_keys('YOUR EMAIL-ADDRESS')
elem_username.send_keys(Keys.RETURN)
sleep(2) #Has to sleep otherwise locating of next element fails.
elem_password = driver.find_element_by_name('password')
elem_password.send_keys('YOUR PASSWORD')
elem_password.send_keys(Keys.RETURN)
