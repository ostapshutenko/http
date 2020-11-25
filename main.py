from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
"""
driver.get('https://account.mail.ru/login')
#elem = driver.find_element_by_class_name('ProvidersListItemIcon ProvidersListItemIconOther ProvidersListItemIconResponsive')
#elem.send_keys(Keys.ENTER)
elem = driver.find_elements_by_class_name('c0171')


elem.send_keys('ostapshutenko')
elem.send_keys(Keys.ENTER)
elem = driver.find_element_by_name('password')
elem.send_keys('XFNcsmP7')
elem.send_keys(Keys.ENTER)
driver.get('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
"""

# пришлось яндекс почту использовать, потому что другие почты банет браузер, говорит, что он не безопасен

driver.get('https://passport.yandex.ru/auth?from=mail&origin=hostroot_homer_auth_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1')

elem = driver.find_elements_by_name('login')
elem[0].send_keys('ostap.shutenko')
elem[0].send_keys(Keys.ENTER)
time.sleep(1)
elem = driver.find_element_by_id('passp-field-passwd')
elem.send_keys('')
elem.send_keys(Keys.ENTER)
time.sleep(3)

while (True):
    elem = driver.find_element_by_class_name('b-link_scroll-right')

    elem = driver.find_elements_by_class_name('mail-MessageSnippet')
    s = list()
    for i in elem:
        s.append(i.get_attribute('href'))
    #print(s)
    data = {
        'name':[],
        'tema':[],
        'data':[],
        'text':[]
    }
    for i in s:
        driver.get(i)
        time.sleep(1)
        elem = driver.find_element_by_class_name('mail-Message-Sender-Email')
        data['name'].append(elem.get_attribute('title'))
        elem = driver.find_element_by_class_name('mail-Message-Toolbar-Subject_message')
        data['tema'].append(elem.text)
        elem = driver.find_element_by_class_name('mail-Message-Date')
        data['data'].append(elem.text)
        elem = driver.find_element_by_class_name('mail-Message-Body-Content')
        data['text'].append(elem.text)
        driver.back()

        #elem = driver.find_element_by_class_name('b-link_scroll-right')
        #nextx = elem.get_attribute('href')
        #if nextx == '':
        #    break
        #elem.click()
print(data)
"""
driver.get('https://www.mvideo.ru/?cityId=CityR_41')
time.sleep(2)
elem = driver.find_elements_by_class_name('next-btn')


elem = driver.find_elements_by_tag_name('ul')
j = 0
for i in elem:
    print(j)
    j+=1
    pprint(i.text)

"""


"""
profile = driver.find_element_by_class_name('avatar')
driver.get(profile.get_attribute('href'))

edit_profile = driver.find_element_by_class_name('text-sm')
driver.get(edit_profile.get_attribute('href'))

gender = driver.find_element_by_name('user[gender]')
select_gender = Select(gender)
select_gender.select_by_value('1')

gender.submit()
"""
#driver.back()
#driver.forward()
#driver.refresh()

driver.quit()