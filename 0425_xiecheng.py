from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=option)
driver.get('https://www.ctrip.com/')
driver.maximize_window()
sleep(1)
driver.find_element(By.CSS_SELECTOR, '.tl_nfes_home_header_register_eTWYU').click()
driver.find_element(By.LINK_TEXT, '同意并继续').click()
dropBtn = driver.find_element(By.CLASS_NAME, 'cpt-drop-btn')
slideCode = driver.find_element(By.ID, 'slideCode')
ac = ActionChains(driver)
sleep(1)
ac.drag_and_drop_by_offset(dropBtn, slideCode.size['width'], 0)
ac.perform()