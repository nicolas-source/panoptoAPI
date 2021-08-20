from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import getpass

import os
from os.path import abspath
from inspect import getsourcefile



# ----Obtaining chromedriver
file_path = abspath(getsourcefile(lambda _: None))
file_dir = os.path.normpath(file_path + os.sep + os.pardir)
print(file_dir)
chromedriver = file_dir + "/chromedriver"


# driver = webdriver.Chrome()
driver = webdriver.Chrome(chromedriver)

driver.get("https://ubc.ca.panopto.com/Panopto/Pages/Auth/Login.aspx?ReturnUrl=https%3A%2F%2Fubc.ca.panopto.com%2FPanopto%2FPages%2FSessions%2FList.aspx%23isMyFolder%3Dtrue")

driver.find_element_by_xpath('//*[@id="usernameInput"]').send_keys("nzheng8")

print("Enter Password:\n")
password = getpass.getpass()

driver.find_element_by_xpath('//*[@id="passwordInput"]').send_keys(str(password))

driver.find_element_by_xpath('//*[@id="PageContentPlaceholder_loginControl_LoginButton"]').click()

driver.get("https://ubc.ca.panopto.com/Panopto/Pages/Sessions/List.aspx#status=%5B1%5D&maxResults=1450&page=0")

# Reaches 'Scheduled" tab here

print("I'm done")

# driver.close()