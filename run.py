from selenium import webdriver
from common import method
from testdata import data

driver = webdriver.Chrome()
driver.implicitly_wait(10)
name = data.test_data.get("name")
passwd = data.test_data.get("passwd")
key = data.test_data.get("key")
num = method.search(driver, name, passwd, key)
print(num)
