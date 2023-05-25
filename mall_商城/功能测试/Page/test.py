import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://192.168.31.162:8090/#/login")
driver.maximize_window()
time.sleep(2)
i = 0
driver.find_element(By.NAME, "username").click()
while i < 5:
    driver.find_element(By.NAME, "username").send_keys(Keys.BACKSPACE)
    i += 1
time.sleep(2)
driver.find_element(By.NAME, "username").send_keys("fuhao")
driver.find_element(By.NAME, "password").send_keys("123")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".el-form-item__content>.el-button--primary").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div/ul/div/li[1]/div/span").click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/ul/div/li[1]/ul/a[2]/li/span').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".el-cascader__label").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.el-cascader-menu>.el-cascader-menu__item').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[2]/ul[2]/li[2]').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.el-select__caret').click()
time.sleep(3)
