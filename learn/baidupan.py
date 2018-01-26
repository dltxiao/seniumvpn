from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Ie()
driver.get("https://pan.baidu.com/")

driver.find_element_by_xpath("//*/div[@class='account-title']/a").click()
driver.find_element_by_xpath("//*/input[@id='TANGRAM__PSP_4__userName']").clear()
driver.find_element_by_xpath("//*/input[@id='TANGRAM__PSP_4__userName']").send_keys('13072723917')
driver.find_element_by_xpath("//*/input[@id='TANGRAM__PSP_4__password']").send_keys('xs3652302')
driver.find_element_by_xpath("//*/input[@id='TANGRAM__PSP_4__submit']").click()

ebook = driver.find_element_by_xpath('//*[@id="layoutMain"]/div/div[2]/div/div[3]/div/div/dd[3]/div[2]/div[1]/a')
#dd.g-clearfix:nth-child(3) > div:nth-child(3) > div:nth-child(1) > a:nth-child(1)
#dd.g-clearfix:nth-child(2) > div:nth-child(3) > div:nth-child(1) > a:nth-child(1)
#//*[@id="layoutMain"]/div/div/div[2]/div/div/div[3]/div/div/dd[3]/div[2]/div[1]/a
#/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div/div/dd[3]/div[2]/div[1]/a
#<a href="javascript:void(0);" class="avr1JMg" title="电子书">电子书</a>
ActionChains(driver).context_click(ebook).perform()
