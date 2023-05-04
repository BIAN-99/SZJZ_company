from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import unittest


class LoginTestCase(unittest.TestCase):
    def inputlogin(self, users):
        self.driver.find_element(By.ID, 'username').send_keys(users['name'])
        self.driver.find_element(By.ID, 'password').send_keys(users['pass'])
        self.driver.find_element(By.CSS_SELECTOR, '.loginButton').click()
        self.driver.implicitly_wait(1)

    @classmethod
    def setUpClass(cls):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('detach', True)
        cls.driver = webdriver.Chrome(options=option)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get('http://192.168.31.162:8889')
        self.driver.maximize_window()

    def tearDown(self):
        message = self.driver.find_element(By.CSS_SELECTOR, '.el-message__content').get_property("innerText")
        if message == "登录成功":
            dropdownList = self.driver.find_element(By.CSS_SELECTOR, '.el-dropdown-link')
            # 创建动作链
            ac = ActionChains(self.driver)
            # 移动到下拉菜单
            ac.move_to_element(dropdownList)
            # 执行
            ac.perform()
            sleep(1)
            logout = self.driver.find_element(By.CSS_SELECTOR, '.el-dropdown-menu__item--divided')
            logout.click()
            sleep(1)
            confirm = self.driver.find_element(By.CSS_SELECTOR, '.el-message-box__btns > .el-button--primary')
            confirm.click()
        else:
            self.driver.refresh()

    def test_001_loginOK(self):
        users = {'name': 'fuhao', 'pass': '123'}
        self.inputlogin(users)
        sleep(1)
        message = self.driver.find_element(By.CSS_SELECTOR, '.el-message__content').get_property("innerText")
        self.assertEqual(message, '登录成功')
        print("正例1:登陆成功")

    def test_002_loginNoID(self):
        users = {'name': '', 'pass': '123'}
        self.inputlogin(users)
        sleep(1)
        message = self.driver.find_element(By.CSS_SELECTOR, '.el-message__content').get_property("innerText")
        self.assertTrue(message == '请输入完整信息!')
        print("反例1:未输入用户名")

    def test_003_loginNoPass(self):
        users = {'name': 'fuhao', 'pass': ''}
        self.inputlogin(users)
        sleep(1)
        message = self.driver.find_element(By.CSS_SELECTOR, '.el-message__content').get_property("innerText")
        self.assertTrue(message == '请输入完整信息!')
        print("反例2:未输入密码")

    def test_004_loginNoAll(self):
        users = {'name': '', 'pass': ''}
        self.inputlogin(users)
        sleep(1)
        message = self.driver.find_element(By.CSS_SELECTOR, '.el-message__content').get_property("innerText")
        self.assertTrue(message == '请输入完整信息!')
        print("反例2:未输入用户名和密码")

    def test_005_loginErrorPass(self):
        users = {'name': 'fuhao', 'pass': '456'}
        self.inputlogin(users)
        sleep(1)
        message = self.driver.find_element(By.CSS_SELECTOR, '.el-message.el-message--error').get_property("innerText")
        self.assertTrue(message == "用户名或者密码输入错误，请重新输入!")
        print("反例4:密码错误")

    def test_006_loginErrorID(self):
        users = {'name': 'abc', 'pass': '123'}
        self.inputlogin(users)
        sleep(1)
        message = self.driver.find_element(By.CSS_SELECTOR, '.el-message.el-message--error').get_property("innerText")
        self.assertTrue(message == "用户名或者密码输入错误，请重新输入!")
        print("反例5:用户名错误")


if __name__ == '__main__':
    unittest.main()
