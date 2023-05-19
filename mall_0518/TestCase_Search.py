import unittest

from ddt import ddt, file_data

from mall_0518.SearchPage import SearchPage

@ddt
class TestSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = SearchPage()
        self.driver.open_url(SearchPage.url)
        self.driver.login()

    def tearDown(self) -> None:
        self.driver.close()

    @file_data("product.yaml")
    def test_search(self, product):
        self.driver.toproductli()
        self.driver.search(product)
        self.assertIsNotNone(self.driver.getinfo())
        print(f"-----搜索商品{product}测试成功!-----")


