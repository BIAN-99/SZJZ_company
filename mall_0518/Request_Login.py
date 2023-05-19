import unittest
import requests
from ddt import ddt, file_data


@ddt
class Test_requests(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()

    def tearDown(self) -> None:
        self.session.close()

    @file_data("login_info.json")
    def test_login(self, username, password):
        params_login = {
            "username": username,
            "password": password
        }
        response = self.session.get("http://192.168.31.162:8090/#/login", params=params_login)
        msg = response.status_code
        self.assertEqual(msg, 200)
        print(f"-----用户:{username},登录测试通过!-----")


if __name__ == '__main__':
    unittest.main()
