#!/usr/bin/python3
"""
# -*- coding: utf-8 -*-
# @Time    : 2018/10/13 19:12
# @Author  : wly
# @Email   : 787115719@qq.com
# @File    : test_alpha_trend.py
# @Software: PyCharm
"""
import unittest
from jqdatasdk import *
from rstrade.util import rs_date
from rstrade.jqdata import alpha_trend
from rstrade.jqdata import rs_fut_const as rs_const
from rstrade.jqdata import rs_conn_jqdata
rs_conn_jqdata.auth('15916406969','a456789')#依次输入账号、密码，链接到平台数据库
class Test(unittest.TestCase):

    def set_data(self):
        self.contracts = rs_const.CONTRACTS_MAIN
        self.startdate = '2018-7-12'
        self.enddate = rs_date.get_tomorow()
        self.feq = '60m'
        self.whitch_ma=50


    def test__get_count_position_of_ma(self):
        self.set_data()
        alpha_trend._get_count_position_of_ma(self.contracts,self.startdate,self.enddate,self.feq,self.whitch_ma)
    def test_get_count_crossing_change_cycle(self):
        alpha_trend._get_count_crossing_change_cycle()


if __name__ == "__main__":
    unittest.main()