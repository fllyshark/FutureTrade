#!/usr/bin/python3
"""
# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 19:08
# @Author  : wly
# @Email   : 787115719@qq.com
# @File    : test_billoard.py
# @Software: PyCharm
"""
import unittest
import rstrade.stock.billboard as fd


class Test(unittest.TestCase):

    def set_data(self):
        self.date = '2015-06-12'
        self.days = 10


    def test_cap_tops(self):
        self.set_data()
        print(fd.cap_tops(self.days))
"""
    def test_broker_tops(self):
        self.set_data()
        print(fd.broker_tops(self.days))

    def test_inst_tops(self):
        self.set_data()
        print(fd.inst_tops(self.days))

    def test_inst_detail(self):
        print(fd.inst_detail())
"""

if __name__ == "__main__":
    unittest.main()