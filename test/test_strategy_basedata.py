#!/usr/bin/python3
"""
# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 17:34
# @Author  : wly
# @Email   : 787115719@qq.com
# @File    : test_strategy_basedata.py
# @Software: PyCharm
"""
import unittest
from jqdatasdk import *
from rstrade.util import rs_date
from rstrade.jqdata import alpha_trend
from rstrade.jqdata import rs_fut_const as rs_const
from rstrade.jqdata import rs_conn_jqdata
from rstrade.analyse import strategy_basedata as macount

rs_conn_jqdata.auth('15916406969','a456789')#依次输入账号、密码，链接到平台数据库
class Test(unittest.TestCase):

    def set_data(self):
        self.contracts = rs_const.C_MAIN_BLACK
        self.startdate = '2018-8-12'
        self.enddate = rs_date.get_tomorow()
        self.freq = '60m'
        self.which_ma=51
    def test_writeBaseDataToFile(self):
        self.set_data()
        macount.writeMADataToFile(self.contracts,self.startdate,self.enddate,self.freq,self.which_ma)


if __name__ == "__main__":
    unittest.main()
