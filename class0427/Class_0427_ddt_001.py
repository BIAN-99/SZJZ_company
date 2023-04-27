import unittest

from ddt import ddt, data, unpack


# 实例化工具类
from class0427.ReadTestData import ReadTestDataUtil

read_test_data = ReadTestDataUtil()


@ddt
class TestPhone(unittest.TestCase):
    # * 表示 这个数据是一个列表

    @data(*read_test_data.read_json('phoneNum.json'))
    def test_001(self, phone):
        print("测试手机号 : ", phone)

    @data(*read_test_data.read_json('userinfo.json'))
    @unpack
    def test_003(self, username, password):
        # print("测试的用户名:", username, "\t 测试的密码:", password)
        print('测试的用户名 : ', username)
        print('测试的密码 : ', password)


if __name__ == "__main__":
    unittest.main()
