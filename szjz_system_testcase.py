import json
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

# 获取浏览器设置对象
option = webdriver.EdgeOptions()

# 设置浏览器不自动退出
option.add_experimental_option('detach', True)

# 获取浏览器,并把以上设置传入

driver = webdriver.Edge(options=option)

# 获取浏览地址并打开
# 登录系统
url = 'http:192.168.31.162:8889'
driver.get(url)
sleep(1)
driver.maximize_window()
get_uname = driver.find_element(By.CSS_SELECTOR, '[placeholder = "请输入用户名"]')
get_uname.click()
get_uname.send_keys('fuhao')
get_pass = driver.find_element(By.CSS_SELECTOR, '[placeholder = "请输入密码"]')
get_pass.click()
get_pass.send_keys('123')
sleep(3)
get_pass.send_keys(Keys.ENTER)
sleep(2)
case_total, case_pass, case_wrong = 0, 0, 0
# ----------测试正例----------
# 测试使用的数据
customer = {'姓名': '济南彭于晏', '联系方式': '16549569356', '年龄': '23', '毕业院校': '清北大学', '专业': '健身'}
# 使用多个class时每个前面都有"."
driver.find_element(By.CSS_SELECTOR, '.fa.fa-money').click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, ".is-opened > .el-menu--inline > .el-menu-item").click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, '.el-icon-plus').click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, '#name').send_keys(customer['姓名'])
sleep(1)
driver.find_element(By.CSS_SELECTOR, '.el-radio__input>.el-radio__inner').click()
driver.find_element(By.CSS_SELECTOR, '[placeholder = "请输入联系方式"]').send_keys(customer['联系方式'])
driver.find_element(By.ID, 'age').send_keys(customer['年龄'])
driver.find_element(By.ID, 'school').send_keys(customer['毕业院校'])
driver.find_element(By.ID, 'major').send_keys(customer['专业'])
driver.find_element(By.ID, 'origin').click()
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[4]/span[text()="智联投递"]').click()
driver.find_element(By.ID, 'degree').click()
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]/span[text()="本科"]').click()
driver.find_element(By.ID, 'employeeGW').click()
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li[1]/span[text()="娟娟"]').click()
driver.find_element(By.CSS_SELECTOR, '.dialog-footer>button.el-button.el-button--primary').click()
if driver.find_element(By.CSS_SELECTOR, '.el-message>.el-message__content').get_property('innerText') == '添加成功':
    case_total += 1
    case_pass +=1
    print("测试通过!!!")
else:
    case_total += 1
    case_wrong += 1
    print("测试未通过!!!")
driver.quit()
print(f"共{case_total}个测试用例,测试通过{case_pass}个,测试未通过{case_wrong}个")



