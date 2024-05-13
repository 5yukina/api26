import unittest,requests
from lib.db1 import *
name = "test"
noname = "peter"

class MyTestCase(unittest.TestCase):
    url = "http://127.0.0.1:8000/api/student/user/register"
    def test_reg_ok(self):
        if check_user(noname):#检查noname是否已经在数据库中
            del_user(noname)#如果已经存在 就删除
        data = {"userName":noname,"password":"123456","userLevel":1}
        r = requests.post(url=self.url,json=data)
        result = {"code":1,"message":"成功","response":None}#预期结果
        self.assertDictEqual(result,r.json())
        self.assertTrue(check_user(noname))#验证数据库中noname是否已存在
        del_user(noname)#清理
    def test_reg_err(self):
        if not check_user(name):#判断name是否已经在数据库中
            add_user(name,"123456")#如梭没有就添加进入
        data = {"userName": name, "password": "123456", "userLevel": 1}
        r = requests.post(url=self.url, json=data)
        result = {"code":2,"message":"用户已存在","response":None}  # 预期结果
        self.assertDictEqual(result, r.json())


if __name__ == '__main__':
    unittest.main()

