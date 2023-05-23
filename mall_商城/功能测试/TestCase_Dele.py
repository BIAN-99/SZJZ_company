import unittest

from ddt import ddt, file_data

from mall_商城.功能测试.Page.DelePage import DelePage


@ddt
class TestDele(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = DelePage()
        self.driver.open_url(DelePage.url)
        self.driver.login()

    @file_data("data/dele.yaml")
    def test_dele(self, product):
        self.driver.toproductli()
        self.driver.search(product)
        self.driver.dele()
        self.assertEqual(self.driver.getinfo(), "删除成功")
        print(f"-----商品{product}删除测试成功!-----")


