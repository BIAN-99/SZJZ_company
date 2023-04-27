import unittest

from ddt import ddt, data, unpack

# 实例化工具类
from class0427.ReadTestData import ReadTestDataUtil

read_test_data = ReadTestDataUtil()


@ddt
class TestPhone(unittest.TestCase):
    # * 表示 这个数据是一个列表

    @data(*read_test_data.read_json('phoneNum.json'))
    def test_001_num(self, phone):
        print("测试手机号 : ", phone)

    @data(*read_test_data.read_json('userinfo.json'))
    @unpack
    def test_002_info(self, username, password):
        # print("测试的用户名:", username, "\t 测试的密码:", password)
        print('测试的用户名 : ', username)
        print('测试的密码 : ', password)

    @data(*read_test_data.read_txt_for_many('name.txt'))
    def test_003_name(self, name):
        print("姓名:", name)


if __name__ == "_main__":
    unittest.main()
