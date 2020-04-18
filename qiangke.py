from selenium import webdriver
import re
import time


office = 'https://sso.scut.edu.cn/cas/login?service=http%3A%2F%2Fxsjw2018.jw.scut.edu.cn%2Fsso%2Fdriotlogin'
url = ''
user = '201930020155'
password = 'Lcg657286329'
subject = '庄子寓言及其智慧'
grade = '2019'
college = '"机械与汽车工程学院"'
driver = webdriver.Chrome()


def get_url(user, password):
    driver.get(office)
    find('//input[@class="login_box_input person"]').send_keys(user)
    find('//input[@type="password"]').send_keys(password)
    find('//*[@class="login_box_landing_btn"]').click()
    finds('//a[@id="drop1"]')[1].click()
    find('//li[a="自主选课"]/a').click()
    driver.switch_to.window(driver.window_handles[-1])
    url = driver.current_url
    return url
# print(url)


def get_goal_subject(url):
    # 获取所有课程
    # find('//li[@class="col-sm-1 col-md-1"]/a').click()
    find('//li[a='+grade+']/a').click()
    # find('//li[@index="jg_id_list_30"]/a').click()
    find('//li[a=' + college + ']/a').click()
    find('//button[@name="query"]').click()
    # 展开
    find('//div[@id="more"]/font/a').click()
    time.sleep(1)
    sub_list = finds('//h3[@class="panel-title"]/span/a')
    def get_order():
        for i in sub_list:
            if i.text == subject:
                return sub_list.index(i) - 1
        return 0
    order = get_order()
    # print('order:', order)
    list_1 = finds('//a[@class="expand_close expand1"]')
    list_1[order].click()
    time.sleep(0.1)
    subjects_list = finds('//div/div/div/table/tbody')
    class_list = subjects_list[order+1].find_elements_by_xpath('./tr[@class="body_tr"]')
    print('classs', len(class_list))
    for each in class_list:
        btn = each.find_element_by_xpath('./td/button[@class="btn btn-primary btn-sm"]')
        # span = btn.find_element_by_tag_name('span')
        # if each.find_element_by_xpath('./td[@class="full"]').text != '已满' and btn.text == '选课':
        if btn.text == '选课':
            print('index', class_list.index(each))
            btn.click()
            try:
                find('//button[@class="bootbox-close-button btn-sm close bootbox-close"]').click()
                # pass
            except:
                # if btn.text == '退选':
                #     print('已选上')
                #     return 1
                print(btn.text)
                return 1
    return 0

def find(object):
    return driver.find_element_by_xpath(object)
def finds(object):
    return driver.find_elements_by_xpath(object)

def main():
    url = get_url(user, password)
    while True:
        if get_goal_subject(url)==1:
            break
main()