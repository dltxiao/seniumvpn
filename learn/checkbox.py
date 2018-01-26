from selenium import webdriver
import os, time

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('./page/checkbox.html')
driver.get(file_path)

inputs = driver.find_elements_by_tag_name('input')

for i in inputs:
    if i.get_attribute('type') == 'checkbox':
        i.click()
        
time.sleep(2)
driver.quit()