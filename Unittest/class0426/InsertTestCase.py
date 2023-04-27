from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest


class InsertTestCase(unittest.TestCase):

    def inputData(self, customer):
        self.driver.find_element(By.ID, 'name').send_keys(customer['name'])
        self.driver.find_element(By.CSS_SELECTOR, '.el-radio__input>.el-radio__inner').click()
        self.driver.find_element(By.ID, 'phone').send_keys(customer['phone'])
        self.driver.find_element(By.ID, 'age').send_keys(customer['age'])
        self.driver.find_element(By.ID, 'school').send_keys(customer['school'])
        self.driver.find_element(By.ID, 'major').send_keys(customer['major'])
        self.driver.find_element(By.ID, 'origin').click()
        sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[4]/span[text()="智联投递"]').click()
        self.driver.find_element(By.ID, 'degree').click()
        sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]/span[text()="本科"]').click()
        self.driver.find_element(By.ID, 'employeeGW').click()
        sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li[1]/span[text()="娟娟"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.dialog-footer>button.el-button.el-button--primary').click()

    @classmethod
    def setUpClass(cls):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('detach', True)
        cls.driver = webdriver.Chrome(options=option)
        cls.driver.get('http://192.168.31.162:8889')
        cls.driver.maximize_window()
        cls.driver.find_element(By.ID, 'username').send_keys('fuhao')
        cls.driver.find_element(By.ID, 'password').send_keys('123')
        cls.driver.find_element(By.CSS_SELECTOR, '.loginButton').click()
        sleep(2)
        # 隐式等待
        cls.driver.implicitly_wait(10)
        # 点击菜单
        cls.driver.find_element(By.CSS_SELECTOR, '.fa-money').click()
        cls.driver.find_elements(By.CSS_SELECTOR, '.is-opened>.el-menu>.el-menu-item')[0].click()
        sleep(1)

    def setUp(self):
        self.driver.find_element(By.CSS_SELECTOR, '.el-icon-plus').click()

    # def tearDown(self):
    #     message2 = self.driver.find_element(By.CSS_SELECTOR, '.el-message>.el-message__content').get_property("innerText")
    #     message
    #     if message2 == "添加成功":
    #         self.driver.find_element(By.CSS_SELECTOR, '.el-icon-plus').click()
    #     else if :
    #         self.driver.refresh()

    def test_001_insertOK(self):
        customer = {'name': '哈哈', 'phone': 57987807344, 'age': 20, 'school': '清华池', 'major': '搓系'}
        self.inputData(customer)
        message = self.driver.find_element(By.CSS_SELECTOR, '.el-message>.el-message__content')
        self.assertEqual(message.get_property('innerText'), "添加成功")

    def test_002_insertOK_otherSchool(self):
        customer = {'name': '呵呵', 'phone': 59760807601, 'age': 20, 'school': '中国政法大学', 'major': '搓系'}
        self.inputData(customer)
        message = self.driver.find_element(By.CSS_SELECTOR, '.el-message>.el-message__content')
        self.assertEqual(message.get_property('innerText'), "添加成功")

    # 反例

    def test_3_insertNotOK(self):
        customer = {'name': '郭', 'phone': 29730807781, 'age': 20, 'school': '中国政法大学', 'major': '搓系'}
        self.inputData(customer)
        message = self.driver.find_element(By.CSS_SELECTOR, '[for="name"]>.el-form-item__content>.el-input+el-form-item__error')
        self.assertEqual(message.get_property('innerText'), "姓名在2-8个字符之间")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
