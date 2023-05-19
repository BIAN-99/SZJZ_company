#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://192.168.31.162:8090/#/login")
driver.maximize_window()
time.sleep(5)
i = 0
while i < 5:
    driver.find_element(By.NAME, "username").send_keys(Keys.BACKSPACE)
    i += 1
driver.find_element(By.NAME, "username").send_keys("fuhao")
driver.find_element(By.NAME, "password").send_keys("123")
button = driver.find_element(By.CSS_SELECTOR, ".el-form-item__content>.el-button--primary")
button.click()
time.sleep(10)
a = driver.find_element(By.CSS_SELECTOR, ".el-submenu>.el-submenu__title")
a.click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div/ul/div/li[1]/ul/a[3]/li").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".btn-add").click()
time.sleep(10)

