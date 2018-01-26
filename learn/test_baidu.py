#coding=utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
from time import sleep

driver.set_window_size(480, 800)
sleep(2)
driver.maximize_window()

###  第一个例子
driver.get('http://www.baidu.com')
#driver.find_element_by_id('kw').send_keys('Selenium2')
#driver.find_element_by_id('su').click()


### 八种定位元素方法学习
#1.id定位
#driver.find_element_by_id('kw').send_keys('Selenium2')
#driver.find_element_by_id('su').click()

#2.name定位
#driver.find_element_by_name('wd').send_keys('Selenium2')
#driver.find_element_by_id('su').click()

#3.class定位
#driver.find_element_by_class_name('s_ipt').send_keys('Selenium2')
#driver.find_element_by_class_name('s_btn').click()  #百度网页中提交按钮的类为复合类class="bg s_btn",selenium不支持复合类，只能选择其中一个

#4.tag定位
#driver.find_element_by_tag_name('input') #重复tag多，难以准确定位

#5.link text定位
#driver.find_element_by_link_text('新闻').click()

#6.partial link定位。 对link定位的补充，有些文本链接比较长，可以只选择能唯一表示此链接的一部分文本
#driver.find_element_by_partial_link_text('闻').click()

#7.xpath定位
#7.1 绝对路径定位
#driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/span[1]/input').send_keys('test')
#driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/span[1]/input').click()

#7.2 元素属性定位
#driver.find_element_by_xpath('//*[@id="kw"]').send_keys('Selenium2')
#driver.find_element_by_xpath('//*[@id="su"]').click()

#7.3 层级与属性结合定位
#driver.find_element_by_xpath("//form[@id='form']/span[1]/input").send_keys('test')
#driver.find_element_by_xpath("//form[@id='form']/span[2]/input").click()

#7.4 使用逻辑运算符
#如果一个属性不能唯一地区分一个元素，可以使用逻辑运算符连接多个属性
#driver.find_element_by_xpath("//input[@id='kw' and @class='s_ipt']").send_keys('test')

#8.CSS定位
#通过class属性定位
#driver.find_element_by_css_selector('.s_ipt')
#driver.find_element_by_css_selector('.bg s_btn')

########### 浏览器操作
#sleep(2)
#driver.back()
#sleep(2)
#driver.forward()
#driver.refresh()


button = driver.find_element_by_xpath('//*[@id="su"]')
ActionChains(driver).context_click(button).perform()
above = driver.find_element_by_partial_link_text('设置')
ActionChains(driver).move_to_element(above).perform()

sleep(2)
driver.quit()