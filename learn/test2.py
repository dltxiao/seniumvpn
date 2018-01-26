from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Ie()
driver.get("https://172.18.5.111")

driver.find_element_by_id("overridelink").click()
driver.find_element_by_xpath("//img[@src='/no1/images/passwd.gif']").click()