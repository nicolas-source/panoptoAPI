from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import csv
import getpass
import time

import os
from os.path import abspath
from inspect import getsourcefile

# ----Obtaining chromedriver_mac
file_path = abspath(getsourcefile(lambda _: None))
file_dir = os.path.normpath(file_path + os.sep + os.pardir)
print(file_dir)
chromedriver = file_dir + "/chromedriver_linux"

# driver = webdriver.Chrome()
driver = webdriver.Chrome(chromedriver)

driver.get(
    "https://ubc.ca.panopto.com/Panopto/Pages/Auth/Login.aspx?ReturnUrl=https%3A%2F%2Fubc.ca.panopto.com%2FPanopto%2FPages%2FSessions%2FList.aspx%23isMyFolder%3Dtrue")

driver.find_element_by_xpath('//*[@id="usernameInput"]').send_keys("nzheng8")

print("Enter Password:\n")
password = getpass.getpass()

driver.find_element_by_xpath('//*[@id="passwordInput"]').send_keys(str(password))

driver.find_element_by_xpath('//*[@id="PageContentPlaceholder_loginControl_LoginButton"]').click()
time.sleep(2)
# driver.get("https://ubc.ca.panopto.com/Panopto/Pages/Sessions/List.aspx#status=%5B1%5D&maxResults=100&page=0")

# buttons = driver.find_elements_by_name('ctl00$ModalContentPlaceHolder$ctl13')
# buttons = driver.find_elements_by_css_selector("#ModalContentPlaceHolder_processManagement > div:nth-child(2) > div.modal-subtitle > input[type=submit]")
# buttons = driver.find_element_by_class_name('settings-action session-action')
# buttons = driver.find_element_by_xpath('/html/body/form/div[3]/div[6]/div/div[1]/div[3]/div[1]/table[2]/tbody/tr[2]/td[3]/div[6]/div[1]/div/a[1]')

# buttons = driver.find_element_by_link_text('Settings')
# buttons = driver.find_element_by_partial_link_text('Settings')
# buttons = driver.find_element_by_xpath('//*[@id="e3195ac2-50e6-4319-ab00-acf00065b593"]/td[3]/div[6]/div[1]/div/a[1]/i')
# buttons = driver.find_element_by_xpath('//*[@id="e3195ac2-50e6-4319-ab00-acf00065b593"]/td[3]/div[6]/div[1]/div/a[1]/div')
item = driver.find_element_by_xpath('//*[@id="e3195ac2-50e6-4319-ab00-acf00065b593"]')

buttons = driver.find_element_by_xpath('//*[@id="e3195ac2-50e6-4319-ab00-acf00065b593"]/td[3]/div[6]/div[1]/div/a[1]')


# buttons = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="e3195ac2-50e6-4319-ab00-acf00065b593"]/td[3]/div[6]/div[1]/div/a[1]')))

# def hover(self):
#     wd = driver.connection
#     element = wd.find_element_by_link_text(self.locator)
#     hov = ActionChains(wd).move_to_element(element)
#     hov.perform()

ActionChains(driver).move_to_element(item).perform()

# item.hover()

buttons.click()

time.sleep(1)

manage = driver.find_element_by_link_text('Manage')
manage.click()

time.sleep(2)

# re_process = driver.find_element_by_name('ctl00$ModalContentPlaceHolder$ctl13')
# re_process = driver.find_element_by_xpath('//*[@id="ModalContentPlaceHolder_processManagement"]/div[2]/div[1]/input')

# re_process = driver.find_element_by_name('Re-process')

# re_process = driver.find_element_by_xpath('/html/body/form/div[3]/div[13]/div[2]/div[1]/input')

re_process = driver.find_element_by_css_selector('#ModalContentPlaceHolder_processManagement > div:nth-child(2) > div.modal-subtitle > input[type=submit]')

re_process.click()




print(buttons)
# buttons.click()
# for button in buttons:
#     print(button)

# Reaches 'Scheduled" tab here

# tableBody = driver.find_element_by_xpath('//*[@id="detailsTable"]/tbody')

time.sleep(2)
