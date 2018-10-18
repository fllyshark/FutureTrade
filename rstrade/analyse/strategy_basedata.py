#!/usr/bin/python3
"""
# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 15:12
# @Author  : wly
# @Email   : 787115719@qq.com
# @File    : strategy_basedata.py
# @Software: PyCharm
"""
import datetime
from rstrade.jqdata import alpha_trend as atrend
from rstrade.jqdata import rs_fut_const as rs_const
from rstrade.util import fileUtils as rs_file
from rstrade.jqdata import rs_fut_var as rs_var
def writeMADataToFile(contracts,startdate,endday,freq,which_ma):
    dic=atrend._get_count_contracts_number(contracts,startdate,endday,freq,which_ma)
    forsort=[[v[1][1],v[0]] for v in dic.items()]
    forsort.sort()
    print(forsort)
    tem_filepath = rs_var.v_position_ma_filepathepath % (datetime.date.today().strftime('%Y-%m-%d'),freq)
    rs_file.appendStrToFile(tem_filepath, 'farm\n')
    for v in forsort:
        contract_ma='               %s:%s\n'%(v[1],v[0])
        rs_file.appendStrToFile(tem_filepath, contract_ma)

