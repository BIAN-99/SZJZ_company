import unittest

from ddt import ddt, file_data

from mall_商城.功能测试.Page.DelBrandPage import DelBrandPage


@ddt
class TestDele(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = DelBrandPage()
        self.driver.open_url(DelBrandPage.url)
        self.driver.login()

    @file_data("data/deleBrand.yaml")
    def test_dele(self, brand):
        self.driver.tobrand()
        self.driver.delbrand(brand)
        self.assertEqual(self.driver.getMessage(), "删除成功")
        print(f"-----品牌{brand}删除测试成功!-----")
