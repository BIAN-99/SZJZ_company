from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from mall_商城.功能测试.Page.BasePage import Base


class ButtonPage(Base):
    commodity_locator = (By.CSS_SELECTOR, ".el-submenu>.el-submenu__title")
    commodity_li_locator = (By.XPATH, "//*[@id='app']/div/div[1]/div/ul/div/li[1]/ul/a[1]/li")
    input_product_locator = (By.CSS_SELECTOR, "[placeholder='商品名称']")
    search_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[1]/button[1]/span')
    shangjia_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[3]/table/tbody/tr[1]/td[6]/div/p[1]/div/span')
    newproduct_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[3]/table/tbody/tr[1]/td[6]/div/p[2]/div/span')
    recomm_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[3]/table/tbody/tr[1]/td[6]/div/p[3]/div/span')
    message_locator = (By.CSS_SELECTOR, '.el-message__content')
    username_input_locator = (By.NAME, "username")
    password_input_locator = (By.NAME, "password")
    login_button_locator = (By.CSS_SELECTOR, ".el-form-item__content>.el-button--primary")
    url = "http://192.168.31.162:8090"
    # 封装搜索商品操作
    def searchProduct(self, product):
        self.get_element(self.commodity_locator).click()
        self.get_element(self.commodity_li_locator).click()
        self.get_element(self.input_product_locator).send_keys(product)
        self.get_element(self.search_locator).click()

    # 封装上架操作
    def shangjia(self):
        self.get_element(self.shangjia_locator).click()

    # 封装新品操作
    def newproduct(self):
        self.get_element(self.newproduct_locator).click()

    # 封装新品操作
    def recomm(self):
        self.get_element(self.recomm_locator).click()

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

    # 获取提示信息
    def getMessage(self):
        message = self.get_element(self.message_locator)
        return message.get_property("innerText")
