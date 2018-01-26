from selenium import webdriver
from time import sleep


### 功能模块按钮及对应的子页面xpath
#功能模块
btn_net_manage = {'button':'//*[@id="accordion1"]/div[1]/div[1]'}
btn_cert_manage = {'button':'//*[@id="accordion1"]/div[3]/div[1]'}
btn_auth_user = {'button':'//*[@id="accordion1"]/div[5]/div[1]'}
btn_ipsec_vpn = {'button':'//*[@id="accordion1"]/div[7]/div[1]'}
btn_ssl_vpn = {'button':'//*[@id="accordion1"]/div[9]/div[1]'}
btn_l2tp_vpn = {'button':'//*[@id="accordion1"]/div[11]/div[1]'}
btn_acl_list = {'button':'//*[@id="accordion1"]/div[13]/div[1]'}
btn_msg_filt = {'button':'//*[@id="accordion1"]/div[15]/div[1]'}
btn_defence = {'button':'//*[@id="accordion1"]/div[17]/div[1]'}
btn_log_manage = {'button':'//*[@id="accordion1"]/div[19]/div[1]'}
btn_sys_setting = {'button':'//*[@id="accordion1"]/div[21]/div[1]'}
#网桥设置
net_brige_setting = {'button':'//span[contains(text(), "网桥设置")]', 
                    'iframe':'//iframe[@src="page/netManage/netBridgeSet.html"]',
                    'parent':btn_net_manage}
#用户认证-认证参数
auth_user_parser = {'button':'//*[@id="tree4"]/li[1]/div/div[1]',
                    'parent':btn_auth_user}
#用户认证-认证参数-常规
auth_user_parser_cg= {'button':'//span[text()="常规"]',
                        'iframe':'//iframe[@src="page/authUser/authParam/authOTP.html"]',
                        'parent':auth_user_parser}
local_user_db = {'button':'//span[contains(text(), "本地用户数据库")]', 
                    'iframe':'//iframe[@src="page/authUser/authUserData.html"]',
                    'parent':btn_auth_user}


    
def login_adm():
    driver.find_element_by_css_selector("a#overridelink").click()
    driver.find_element_by_xpath("//*/input[@id='user']").send_keys('adm')
    driver.find_element_by_xpath("//*/input[@id='pwd']").send_keys('adm')
    driver.find_element_by_xpath('//*/img[@src="image/login_btn.png"]').click()
    try:
        driver.find_element_by_xpath('/html/body/div[9]/div[3]/button').click()
    except:
        pass

def get_parent_node(target_page):
#    try:
#        test = target_page['parent']['button']
#        print(test)
#        print(type(driver.find_element_by_xpath(test).get_attribute("class")))
    return target_page['parent']
#    except:
#        return None

def module_page_switch(target_page):
    print('当前target_page: {}'.format(target_page))
    if 'parent' in target_page:
        parent_page = get_parent_node(target_page)
        module_page_switch(parent_page)
    node_stat = driver.find_element_by_xpath(target_page['button']).get_attribute("class")
    print(node_stat)
    if node_stat.find('close'):
        print(driver.find_element_by_xpath(target_page['button']))
        driver.find_element_by_xpath(target_page['button']).click()

    if 'iframe' in target_page:
        driver.switch_to.frame(driver.find_element_by_xpath(target_page['iframe']))
        print('Switch to iframe {} success!'.format(target_page['iframe']))
    print("递归退出，target_page当前为{}".format(target_page))


if __name__ == '__main__':
    driver = webdriver.Ie()
    driver.implicitly_wait(10)
    driver.get("https://172.18.5.111:8888")
    login_adm()
    get_parent_node(local_user_db)


    module_page_switch(net_brige_setting)


