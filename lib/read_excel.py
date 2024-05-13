#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2024-4-23 11:48
# Author:ws
# @File:read_excel.py
# @Software:PyCharm
import xlrd
#
# wb = xlrd.open_workbook("test_user_data.xlsx")
# sheet1 = wb.sheet_by_name("test_user_reg")
#
# print(sheet1.nrows)
#
# print(sheet1.ncols)
#
# print(sheet1.cell(0,0).value)
#
# # print(sheet1.row_values(0))
# # print(dict(zip(sheet1.row_values(0),sheet1.row_values(1))))
# for i in range(sheet1.nrows):
#     print(sheet1.row_values(i))

class readexcel():

    def excel_to_list(self,data_file,sheet):
        wb = xlrd.open_workbook(data_file)
        sheet1 = wb.sheet_by_name(sheet)
        keys = sheet1.row_values(0)
        list1 = []

        for i in range(1,sheet1.nrows):
            j = dict(zip(keys,sheet1.row_values(i)))
            #print(j)
            list1.append(j)
        return list1

    def get_test_data(self,data_list,case_name):
        for case_data in data_list:
            if case_name == case_data['case_name']:
                return case_data


if __name__ == '__main__':
    r = readexcel()
    print(r.excel_to_list("test_user_data.xlsx","test_user_login"))
