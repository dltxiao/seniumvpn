from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Ie()
driver.implicitly_wait(5)
driver.get("https://172.18.5.111:8888")



def login_adm():
    driver.find_element_by_css_selector("a#overridelink").click()
    driver.find_element_by_xpath("//*/input[@id='user']").send_keys('adm')
    driver.find_element_by_xpath("//*/input[@id='pwd']").send_keys('adm')
    driver.find_element_by_xpath('//*/img[@src="image/login_btn.png"]').click()
    sleep(2)
    try:
        driver.switch_to_alert().accept()
#        driver.find_element_by_xpath('/html/body/div[9]/div[3]/button').click()
    except:
        pass

def net_brige_add():
    driver.find_element_by_xpath('//div[@id="add"]').click()


login_adm()

driver.find_element_by_xpath('//span[contains(text(), "网桥设置")]').click()
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@src="page/netManage/netBridgeSet.html"]'))
print('switched success!')



#net_brige_add()
def get_brige_list(driver):
    brgs = driver.find_elements_by_xpath('//tbody/tr')




"""
//a[@onclick="saveConfig();"]               顶栏：保存
//a[@onclick="quit_login();"]               顶栏：退出
//a[@onclick="rebootMess();"]               顶栏：重启
//div[text()="证书管理"]                    导航栏：功能模块选择
//span[contains(text(), "网桥设置")]        导航栏：功能节点选择 
//button[contains(text(), "关闭")]
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@src="page/netManage/netBridgeSet.html"]'))   子功能表单切换
"""
