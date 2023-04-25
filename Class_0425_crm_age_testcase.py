from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=option)
case_total, case_pass, case_error = 0, 0, 0
driver.maximize_window()
# ---------- 添加用户-正例 ----------

driver.get('http://192.168.31.162:8889')
sleep(1)
driver.find_element(By.ID, 'username').send_keys('fuhao')
driver.find_element(By.ID, 'password').send_keys('123')
driver.find_element(By.CSS_SELECTOR, '.loginButton').click()
sleep(1)

# 隐式等待
driver.implicitly_wait(5)
# 点击菜单
driver.find_element(By.CSS_SELECTOR, '.fa-money').click()
driver.find_elements(By.CSS_SELECTOR, '.is-opened>.el-menu>.el-menu-item')[0].click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, '.el-icon-plus').click()
sleep(2)
# 正常录入
# 数据
customer = {'name': '郭德纲', 'phone': 19984687779, 'age': 20, 'school': '清华池', 'major': '搓系'}
driver.find_element(By.ID, 'name').send_keys(customer['name'])
driver.find_element(By.CSS_SELECTOR, '.el-radio__input>.el-radio__inner').click()
driver.find_element(By.ID, 'phone').send_keys(customer['phone'])
driver.find_element(By.ID, 'age').send_keys(customer['age'])
driver.find_element(By.ID, 'school').send_keys(customer['school'])
driver.find_element(By.ID, 'major').send_keys(customer['major'])
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
    case_pass += 1
    print('测试通过')
    print(f'共执行测试用例{case_total}个,通过{case_pass}个,失败{case_error}个')
else:
    case_total += 1
    case_error += 1
    print('测试不通过')
    print(f'共执行测试用例{case_total}个,通过{case_pass}个,失败{case_error}个')
sleep(5)

# ---------- 添加用户-反例-用户名未输入 ----------
# driver.find_element(By.CSS_SELECTOR, '.el-icon-plus').click()
# sleep(2)
# # 正常录入
# # 数据
# customer1 = {'name': '郭德纲', 'phone': 19988887777, 'age': 20, 'school': '清华池', 'major': '搓系'}
# # driver.find_element(By.ID, 'name').send_keys(customer1['name'])
# driver.find_element(By.CSS_SELECTOR, '.el-radio__input>.el-radio__inner').click()
# driver.find_element(By.ID, 'phone').send_keys(customer1['phone'])
# driver.find_element(By.ID, 'age').send_keys(customer1['age'])
# driver.find_element(By.ID, 'school').send_keys(customer1['school'])
# driver.find_element(By.ID, 'major').send_keys(customer1['major'])
# driver.find_element(By.ID, 'origin').click()
# sleep(1)
# driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[4]/span[text()="智联投递"]').click()
# driver.find_element(By.ID, 'degree').click()
# sleep(1)
# driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]/span[text()="本科"]').click()
# driver.find_element(By.ID, 'employeeGW').click()
# sleep(1)
# driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li[1]/span[text()="娟娟"]').click()
# driver.find_element(By.CSS_SELECTOR, '.dialog-footer>button.el-button.el-button--primary').click()
#
# info = driver.find_element(By.CSS_SELECTOR, 'div:has(>#name)+div.el-form-item__error').get_property('innerText')
# if info == '必须填写':
#     case_total += 1
#     case_pass += 1
#     print('测试通过')
#     print(f'共执行测试用例{case_total}个,通过{case_pass}个,失败{case_error}个')
# else:
#     case_error += 1
#     print('测试不通过')
#     print(f'共执行测试用例{case_total}个,通过{case_pass}个,失败{case_error}个')
