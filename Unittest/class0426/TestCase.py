import unittest


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("=====> setupClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("=====> teardownClass")

    def setUp(self):
        print("---------> setup")

    def tearDown(self):
        print("---------> teardown")

    def test_2(self):
        print("testcase2")

    def test_1(self):
        print("testcase1")


if __name__ == '__main__':
    unittest.main()