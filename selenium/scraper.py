from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# driver.close()