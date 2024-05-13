# import logging
# import unittest,requests,json,sys,ast
# from lib.case_log import *
# from lib.read_excel import *
# from config.config import *
#
#
# class BaseCase(unittest.TestCase):
#     r = readexcel()
#     @classmethod
#     def setUpClass(cls):
#         print(cls.__name__)
#         if cls.__name__ != 'BaseCase':
#             cls.data_list = cls.r.excel_to_list(data_file,cls.__name__)
#             print(cls.__name__)
#
#     def get_case_data(self,case_name):
#         return self.r.get_test_data(self.data_list,case_name)
#
#     def send_request(self,case_name):
#         case_data = self.get_case_data(case_name)
#         url = case_data.get('url')
#
#         method = case_data.get('method')
#         headers = case_data.get('headers')
#
#         args = case_data.get('args')
#         data_type = case_data.get('data_type')
#         expect_res = case_data.get('expect_res')
#         print(case_name,url,method,headers,args,data_type,expect_res)
#         if method.upper() == 'GET':
#             logging.info("get data")
#             response =requests.get(url,headers=headers,params=args)
#             print(response.text)
#             log_case_info(case_name,url,args,expect_res,requests.json())
#         elif data_type.upper() == 'JSON':
#             logging.info("post json data")
#             res = requests.post(url=url,json=json.loads(args))
#             print(res.text)
#             log_case_info(case_name,url,args,expect_res,res.json())
#             self.assertIn(expect_res,res.text)
#         elif data_type.upper() == 'FROM':
#             logging.info("post from data")
#             response = requests.post(url, headers=headers, data=args)
#             log_case_info(case_name, url, args, expect_res, requests.json())
#             self.assertIn(expect_res, response.text)
#         else:
#             print("""暂不支持该数据类型""")
#
# if __name__ == '__main__':
#     unittest.main()


import unittest,requests,json,sys,ast
from config.config import *
from lib.read_excel import *
from lib.case_log import log_case_info

sys.path.append("../..")#统一将包的搜索路径提升到项目根目录下

class BaseCase(unittest.TestCase):#继承unittest.TestCase
    r = readexcel()
    @classmethod
    def setUpClass(cls):
        if cls.__name__ !='BaseCase':
            cls.data_list = cls.r.excel_to_list(data_file,cls.__name__)

    def get_case_data(self,case_name):
        return self.r.get_test_data(self.data_list,case_name)

    def send_request(self,case_data):
        case_name = case_data.get('case_name')
        url = case_data.get('url')
        args = case_data.get('args')
        headers = case_data.get('header')
        expect_res = case_data.get('expect_res')
        method = case_data.get('method')
        data_type = case_data.get('data_type')
        if method.upper() == 'GET':#GET类型请求
            res = requests.get(url=url,params=json.loads(args))
        elif data_type.upper() == 'FORM':#表单格式请求
            res = requests.post(url=url,json=json.loads(args),headers=json.loads(headers))
            log_case_info(case_name,url,args,expect_res,res.text)
            self.assertIn(expect_res,res.text)
        elif data_type.upper() == 'JSON':#JSON格式请求
            res = requests.post(url=url,json=json.loads(args),headers=json.loads(headers))
            log_case_info(case_name,url,args,expect_res,res.json())
            self.assertIn(expect_res,res.text)