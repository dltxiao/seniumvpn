from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.youdao.com")

size = driver.find_element_by_xpath("//*/input[@id='translateContent']").size
print(size)
text = driver.find_element_by_xpath("//*/p[@class='phone']").text
print(text)
attribute = driver.find_element_by_xpath("//*/p[@class='phone']").get_attribute('type')
print(attribute)
result = driver.find_element_by_xpath("//*/p[@class='phone']").is_displayed()
print(result)

#driver.find_element_by_xpath("//*/input[@id='translateContent']").send_keys("hello")
#driver.find_element_by_xpath("//*/input[@id='translateContent']").submit()

