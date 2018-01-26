from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
try:
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'ksssw')))
    element.send_keys('selenium')
except:
    print('Test Failed')
    pass

sleep(2)
driver.quit()