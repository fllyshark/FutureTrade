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
import pandas as pd
from rstrade.jqdata import alpha_base_func as base_func
from rstrade.jqdata import rs_fut_const as rs_const
from rstrade.util import fileUtils as rs_file
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
        pds=base_func._join_contracts_cross_ma_close(index, startdate, endday, freq,which_ma)
        position_ma = pds['ma'][0].pop()
        if position_ma== rs_const.C_POSITON_MA_STATUS['_ON_MA']:
            v_count_crosson=v_count_crosson+1
            arr_contracts_on.append(index)
        elif position_ma == rs_const.C_POSITON_MA_STATUS['_BLOW_MA']:
            v_count_crossblow=v_count_crossblow+1
            arr_contracts_blow.append(index)
    str_to_file='[on_ma_count:%s]' \
                '[blow_ma_count:%s]' \
                '[all_ma_count:%s]'\
                %(v_count_crosson,v_count_crossblow,v_count_crosson+v_count_crossblow)
    print(str_to_file)
    one_dict_record={pds.index[0].strftime('%Y-%m-%d %H:%M:%S'):{'on_ma_count':v_count_crosson,'blow_ma_count':v_count_crossblow,
                                                         'all_ma_count':v_count_crosson+v_count_crossblow+1,
                                                         'on_ma_contracts':arr_contracts_on,'blow_ma_contracts':arr_contracts_blow}}
    tem_filepath = rs_var.v_position_ma_filepathepath%(rs_date.today(),freq)
    rs_file.appendDictRecordToFile(tem_filepath,one_dict_record)
#模型1
def _get_count_contracts_number(contracts,startdate,endday,freq,which_ma):
    """

    :param contracts:
    :param startdate:
    :param endday:
    :param freq:
    :param which_ma:
    :return:
    """
    dic=dict()
    for index  in contracts:
        pds=base_func._join_contracts_cross_ma_ago(index, startdate, endday,rs_date.get_tomorow(),freq,which_ma)
        comp = pds.iloc[-1].values[0]
        i=-1
        count=0
        if index=='HC':
            print(pds)
        while(pds['ma'][i] ==comp and len(pds['ma'])>count):
            count=count+1
            i=i-1
        list0=[int(comp),count]
        if index in dic.keys():
            dic.append(list0)
        else:
            dic[index]=list0
    print(dic)
    return dic

#模型二，涨幅
def zhangfu():
    return
#模型三,std
def std():
    return
def _get_count_crossing_change_cycle():
    tem_filepath = rs_var.v_position_ma_filepathepath % (rs_date.today())
    dicts=rs_file.readJsonFile(tem_filepath)
    print(dicts)
def _check_whichday_freq_is_all_in_json(checkdate,freq):
    """
    补齐缺失的数据
    :param checkdate:
    :param freq:
    :return:
    """
    tem_filepath = rs_var.v_position_ma_filepathepath % (checkdate,freq)
    dicts=rs_file.readJsonFile(tem_filepath)
