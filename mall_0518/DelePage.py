from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from mall_0518.BasePage import Base


class DelePage(Base):
    commodity_locator = (By.CSS_SELECTOR, ".el-submenu>.el-submenu__title")
    commodity_li_locator = (By.XPATH, "//*[@id='app']/div/div[1]/div/ul/div/li[1]/ul/a[1]/li")
    input_product_locator = (By.CSS_SELECTOR, "[placeholder='商品名称']")
    info_locator = (By.CSS_SELECTOR, ".el-button--danger")
    search_btn_locator = (By.CSS_SELECTOR, ".el-button--primary")
    del_btn_locator = (By.CSS_SELECTOR, ".el-button--danger")
    confirm_btn_locator = (By.CSS_SELECTOR, ".el-message-box__btns>.el-button--primary")
    info_locator = (By.CSS_SELECTOR, ".el-message--success")
    username_input_locator = (By.NAME, "username")
    password_input_locator = (By.NAME, "password")
    login_button_locator = (By.CSS_SELECTOR, ".el-form-item__content>.el-button--primary")
    url = "http://192.168.31.162:8090"

    # 封装删除操作
    def dele(self):
        self.get_element(self.del_btn_locator).click()
        self.get_element(self.confirm_btn_locator).click()

    # 获取提示信息
    def getinfo(self):
        message = self.get_element(self.info_locator).get_property("innerText")
        return message

        # 登录

    def login(self):
        i = 0
        self.get_element(self.username_input_locator).click()
        while i < 5:
            self.send_keys(self.username_input_locator, Keys.BACKSPACE)
            i += 1
        self.get_element(self.username_input_locator).send_keys("fuhao")
        self.get_element(self.password_input_locator).send_keys("123")
        self.get_element(self.login_button_locator).click()

    # 封装点击到商品列表的函数
    def toproductli(self):
        self.get_element(self.commodity_locator).click()
        self.get_element(self.commodity_li_locator).click()

    # 封装搜索操作
    def search(self, product):
        self.get_element(self.input_product_locator).click()
        self.get_element(self.input_product_locator).send_keys(product)
        self.get_element(self.search_btn_locator).click()
