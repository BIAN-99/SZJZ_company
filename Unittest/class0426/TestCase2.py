import unittest


class MyTestCase(unittest.TestCase):
    # 类前置方法
    @classmethod
    def setUpClass(cls):
        # 读取配置文件
        # 类属性
        cls.ipaddr = '192.168.31.162'
        print("============> setupClass")

    # 类后置方法
    @classmethod
    def tearDownClass(cls):
        print("=============> teardownClass")

    # 前置方法
    def setUp(self):
        print('-------------> setup')

    # 后置方法
    def tearDown(self):
        print('-------------> teardown')

    def test_2(self):
        # 一顿操作
        a = 1
        b = 2
        print('test2')
        print(id(self))
        self.assertNotEqual(a, b, '相等')

    def test_1(self):
        # 一顿操作
        li = {1, 2, 3, 4, 5, 6}
        a = 7
        self.assertNotIn(a, li)
        print(id(self))
        print("test1")

    def test_3(self):
        print('test3', MyTestCase.ipaddr)
        MyTestCase.ipaddr = '192.168.3.128'

        li1 = [1, 2, 3, 4, 5, 6]
        li2 = list(range(1, 7))
        self.assertListEqual(li1, li2)

    def jisuan(self, num1, num2):
        return num1 // num2

    # setInterval(getDate,1000)
    def test_4(self):
        print('test4', MyTestCase.ipaddr)
        self.assertRaises(ZeroDivisionError, self.jisuan, 5, 0)


if __name__ == '__main__':
    unittest.main()
