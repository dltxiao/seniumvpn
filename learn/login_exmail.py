from selenium import webdriver
import time



driver = webdriver.Chrome()
driver.get('https://exmail.qq.com/cgi-bin/loginpage')

def print_info():
    title = driver.title
    print(title)
    now_url = driver.current_url
    print(now_url)

print('Before login:')
print_info()

driver.find_element_by_xpath("//*/input[@id='inputuin']").send_keys("zhongxiao@secway.net.cn")
driver.find_element_by_xpath("//*/input[@id='pp']").send_keys("C@1lmexiao")
driver.find_element_by_xpath("//*/input[@id='btlogin']").click()
time.sleep(5)

print('After login:')
print_info()

driver.quit()