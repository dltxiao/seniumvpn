from selenium import webdriver
from time import sleep

driver = webdriver.Ie()
driver.get("https://172.18.5.111:8888")

def login_adm():
    driver.find_element_by_css_selector("a#overridelink").click()
    driver.find_element_by_xpath("//*/input[@id='user']").send_keys('adm')
    driver.find_element_by_xpath("//*/input[@id='pwd']").send_keys('adm')
    driver.find_element_by_xpath('//*/img[@src="image/login_btn.png"]').click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[9]/div[3]/button').click()
    #driver.find_element_by_xpath('//button[contains(text(), "关闭")]').click()

login_adm()

driver.find_element_by_xpath('//span[contains(text(), "网桥设置")]').click()


"""
//span[contains(text(), "网桥设置")]   #功能节点选择 
//button[contains(text(), "关闭")]
"""
