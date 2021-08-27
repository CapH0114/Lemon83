import time

def login(driver,name,passwd):
    driver.get("http://erp.lemfix.com/login.html")
    driver.maximize_window()
    username = driver.find_element_by_id("username").send_keys(name)
    driver.find_element_by_id("password") .send_keys(passwd)
    driver.find_element_by_id("btnSubmit") .click()



def search(driver,name,passwd,key):
    login(driver,name,passwd)
    driver.find_element_by_css_selector("[title='零售出库']").click()
    id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
    ifid = id + "-frame"

    time.sleep(2)
    driver.switch_to.frame(ifid)

    driver.find_element_by_xpath("//*[@id='searchNumber']").send_keys(key)
    driver.find_element_by_id("searchBtn").click()
    time.sleep(2)
    num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
    return num