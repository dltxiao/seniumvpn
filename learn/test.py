from selenium import webdriver
from selenium.webdriver.support.select import Select
#driver = webdriver.Ie()
driver = webdriver.Chrome()
driver.get("https://172.18.5.111:8888")

driver.find_element_by_id("overridelink").click()

driver.find_element_by_xpath('//*[@id="user"]').send_keys("adm")
driver.find_element_by_id("pwd").send_keys("adm")
driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td[3]/img").click()
driver.find_element_by_xpath("/html/body/div[9]/div[3]/button").click()
driver.find_element_by_xpath("//div[@id='accordion1']/div[7]/div[2]").click()
driver.find_element_by_xpath("//li[@url='page/ipsec/ipsecTunnelCfg.html']/div/span").click()
tunconf_frame = driver
driver.switch_to_frame(id)
driver.find_element_by_xpath("//*[@id='add']")
driver.find_element_by_xpath("//input[@id='end_name']").send_keys("test")
sel = driver.find_element_by_xpath("//select[@id='local_interface']")
Select(sel).select_by_index('1')

#add

#1505293932941