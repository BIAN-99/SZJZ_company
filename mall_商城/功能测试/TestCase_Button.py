import unittest

from ddt import ddt, file_data

from mall_商城.功能测试.Page.ButtonPage import ButtonPage


@ddt
class TestDele(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = ButtonPage()
        self.driver.open_url(ButtonPage.url)
        self.driver.login()

    @file_data("data/product.yaml")
    def test_001_shangjia(self, product):
        self.driver.searchProduct(product)
        self.driver.shangjia()
        self.assertEqual(self.driver.getMessage(), '修改成功')
        print(f"-----商品{product}上架修改测试成功!-----")
        self.driver.newproduct()
        self.assertEqual(self.driver.getMessage(), '修改成功')
        print(f"-----商品{product}新品修改测试成功!-----")
        self.driver.recomm()
        self.assertEqual(self.driver.getMessage(), '修改成功')
        print(f"-----商品{product}推荐修改测试成功!-----")


