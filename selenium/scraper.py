from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


import csv
import getpass
import time

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
time.sleep(2)
driver.get("https://ubc.ca.panopto.com/Panopto/Pages/Sessions/List.aspx#status=%5B1%5D&maxResults=100&page=0")

# Reaches 'Scheduled" tab here

# tableBody = driver.find_element_by_xpath('//*[@id="detailsTable"]/tbody')

time.sleep(2)

tableBodyElements = driver.find_elements_by_class_name("thumbnail-row")

# print(tableBodyElements)

scheduleRecorderIDs = []

for webElement in tableBodyElements:
    # print(webElement.get_attribute("text"))
    scheduleRecorderIDs.append({'Id': webElement.get_attribute('id')})



keys = scheduleRecorderIDs[0].keys()
with open('../folders/csvFiles/scheduledSessionsIdList.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(scheduleRecorderIDs)



# driver.close()