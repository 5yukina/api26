import unittest

def setUpModule():
    print('=== setUpModule ===')
def tearDownModule():
    print('=== tearDownModule ===')

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupclass")
    @classmethod
    def tearDownClass(cls):
        print("teardownclass")
    def setUp(self):
        print("setup")
    def tearDown(self):
        print("teardown")
    def test_01(self):
        print("test01")
        self.assertEqual(True,True)

    def test_02(self):
        print("test02")
        self.assertIn('h','hello')
    def test_03(self):
        print("test03")
        self.assertIsNot(2,4/2)
    def test_04(self):
        print("test04")
        self.assertGreater(7,4)

    def test_05(self):
        print("test05")
        self.assertIsInstance({'user':'stu',"ps":'123'},dict)


if __name__ == '__main__':
    unittest.main()