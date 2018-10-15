#!/usr/bin/python3
"""
# -*- coding: utf-8 -*-
# @Time    : 2018/10/13 19:07
# @Author  : wly
# @Email   : 787115719@qq.com
# @File    : alpha_trend.py
# @Software: PyCharm
"""
import datetime
import json
from rstrade.jqdata import alpha_base_func as base_func
from rstrade.jqdata import rs_fut_const as rs_const
from rstrade.util import fileUtils as u_file
from rstrade.jqdata import rs_fut_var as rs_var
from rstrade.util import rs_date

def _get_count_position_of_ma(contracts,startdate,endday,freq,which_ma):
    """
    计算均线上下合约数
    :return:
    """
    v_count_crosson = 0
    v_count_crossblow=0
    arr_contracts_on=[]
    arr_contracts_blow=[]
    for index in contracts:
        str_stutas=base_func._join_contracts_cross_ma_close(index, startdate, endday, freq,which_ma)
        if str_stutas == rs_const.C_POSITON_MA_STATUS['_ON_MA']:
            v_count_crosson=v_count_crosson+1
            arr_contracts_on.append(index)
        elif str_stutas == rs_const.C_POSITON_MA_STATUS['_BLOW_MA']:
            v_count_crossblow=v_count_crossblow+1
            arr_contracts_blow.append(index)
    str_to_file='[on_ma_count:%s]' \
                '[blow_ma_count:%s]' \
                '[all_ma_count:%s]'\
                %(v_count_crosson,v_count_crossblow,v_count_crosson+v_count_crossblow)
    print(str_to_file)
    one_dict_record={rs_date.today()+'-'+str(rs_date.get_hour()):{'on_ma_count':v_count_crosson,'blow_ma_count':v_count_crossblow,
                                                         'all_ma_count':v_count_crosson+v_count_crossblow+1,
                                                         'on_ma_contracts':arr_contracts_on,'blow_ma_contracts':arr_contracts_blow}}
    tem_filepath = rs_var.v_position_ma_filepathepath%(rs_date.today(),freq)
    u_file.appendDictRecordToFile(tem_filepath,one_dict_record)
def _get_count_crossing_change_cycle():
    tem_filepath = rs_var.v_position_ma_filepathepath % (rs_date.today())
    dicts=u_file.readJsonFile(tem_filepath)
    print(dicts)