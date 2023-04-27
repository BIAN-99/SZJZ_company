from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import unittest


class SearchTestCase(unittest.TestCase):
    def inputname(self, name):
        input_name = self.driver.find_element(By.CSS_SELECTOR, '[placeholder = "通过客户名搜索..."]')
        input_name.send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, '.el-button--primary > .el-icon-search').click()

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
        sleep(1)
        # 隐式等待
        cls.driver.implicitly_wait(10)
        # 点击菜单
        cls.driver.find_element(By.CSS_SELECTOR, '.fa-money').click()
        cls.driver.find_elements(By.CSS_SELECTOR, '.is-opened>.el-menu>.el-menu-item')[0].click()
        sleep(1)

    def setUp(self):
        self.driver.find_element(By.CSS_SELECTOR, '.el-input__inner').click()

    def tearDown(self):
        chains = ActionChains(self.driver)
        chains.move_to_element(self.driver.find_element(By.CSS_SELECTOR, '.el-input__inner'))
        chains.perform()
        self.driver.find_element(By.CSS_SELECTOR, '.el-input__clear').click()
        sleep(2)

    # -------------- 正例 --------------

    def test_001_searchOK(self):
        name = '卞福昊'
        self.inputname(name)
        message = self.driver.find_element(By.CSS_SELECTOR, '.el-pagination__total')
        self.assertIsNotNone(message.get_property("innerText"))
        print("正例1:搜索卞福昊,成功")

    def test_002_searchOK(self):
        name = '芜湖大司马'
        self.inputname(name)
        message = self.driver.find_element(By.CSS_SELECTOR, '.el-pagination__total')
        self.assertIsNotNone(message.get_property("innerText"))
        print("正例2:搜索芜湖大司马,成功")

    # -------------- 反例 --------------

    def test_003_NoSearchOK(self):
        name = '济南吴彦祖'
        self.inputname(name)
        message = self.driver.find_element(By.CSS_SELECTOR, '.el-pagination__total')
        self.assertIsNotNone(message.get_property("innerText"))
        print("反例1:搜索济南吴彦祖,未成功")


if __name__ == '__main__':
    unittest.main()
