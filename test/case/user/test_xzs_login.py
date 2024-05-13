import unittest
from lib import xzs_login


class MyTestCase(unittest.TestCase):
    x = xzs_login.xzs_login()

    def test_login_ok(self):
        t = self.x.login("student","123456")
        #self.assertIn("成功",t)
    def test_login_err(self):
        t = self.x.login("","123456")
        self.assertIn("用户名或密码错误",t)

# class MyTestCase(unittest.TestCase):
#     url = "http://127.0.0.1:8000/api/user/login"
#     header = {
#         "Content-Type":"application/json"
#     }
#     def test_login_ok(self):
#         data = {"userName":"student","password":"123456","remember":False}
#         r = requests.post(url=self.url,headers=self.header,json=data)
#         self.assertIn("成功",r.text)
#
#     def test_login_err(self):
#         data = {"userName":"","password":"123456","remember":False}
#         r = requests.post(url=self.url, headers=self.header, json=data)
#         self.assertIn("用户名或密码错误", r.text)

if __name__ == '__main__':
    unittest.main()
