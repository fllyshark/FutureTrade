#!/usr/bin/python3
"""
# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 20:51
# @Author  : wly
# @Email   : 787115719@qq.com
# @File    : alpha_base_func.py
# @Software: PyCharm
"""
import pandas as pd
from jqdatasdk import *
from rstrade.jqdata import rs_fut_const as rs_const
from rstrade.util import indictor as rs_indictor
from datetime import datetime
from rstrade.util import rs_date
def _join_contracts_cross_ma_close(contract, startdate, enddate, freq,whitch_ma):
    """
    功能：得到当前合约相当MA（）均线的位置，盘中实时
    1，获得单一合约历史数据
    2,计算ma数值
    3,计算相对均线的位置
    注意：endday-startday周期数应满足计算ma的数量，不然ma不对
    :param contracts: 合约简写
    :param startdate: 计算开始日期
    :param endday: 计算结束日期
    :param freq: 计算周期
    :param whitch_ma 多少周期的均线值
    :return: 'NU'--无数据、‘ON’--线上、‘BLOW’--线下
    """
    hsdata = get_price(rs_const.AllCONTRACTS_MAIN[contract], start_date=startdate, end_date=enddate, frequency=freq,
                       skip_paused=True)
    if len(hsdata)<=0:
        print("%s--该合约无数据！exit--\n"%rs_const.AllCONTRACTS_MAIN[contract])
        return rs_const.C_POSITON_MA_STATUS['_NONE_MA']
    print(hsdata.tail(20))
    hsdata=hsdata[:rs_date.get_now()]#默认get_price()会填充当日全部数据，清除未来数据
    print(hsdata.tail(10))
    malast=rs_indictor.ma(hsdata,whitch_ma)#计算均线值
    if hsdata['close'][-1]>malast[-1]:
        return rs_const.C_POSITON_MA_STATUS['_ON_MA']
    else:
        return rs_const.C_POSITON_MA_STATUS['_BLOW_MA']
def _join_contracts_cross_ma_ago(contract, startdate, enddate, whichtime_ago,freq,whitch_ma):
    """
    功能：得到当前合约相当MA（）均线的位置
    1，获得单一合约历史数据
    2,计算ma数值
    3,计算相对均线的位置
    4,which_timeago 要获得过去哪个时间的Ma，位置情况格式"%Y-%m-%d %H:%M:%S"
    注意：endday-startday周期数应满足计算ma的数量，不然ma不对
    :param contracts: 合约简写
    :param startdate: 计算开始日期
    :param endday: 计算结束日期
    :param freq: 计算周期
    :param whitch_ma 多少周期的均线值
    :return: 'NU'--无数据、‘ON’--线上、‘BLOW’--线下
    """
    hsdata = get_price(rs_const.AllCONTRACTS_MAIN[contract], start_date=startdate, end_date=enddate, frequency=freq,
                       skip_paused=True)
    if len(hsdata)<=0:
        print("%s--该合约无数据！exit--\n"%rs_const.AllCONTRACTS_MAIN[contract])
        return rs_const.C_POSITON_MA_STATUS['_NONE_MA']
    hsdata=hsdata[:whichtime_ago]#默认get_price()会填充当日全部数据，清除未来数据
    print(hsdata[:-10])
    malast=rs_indictor.ma(hsdata,whitch_ma)#计算均线值
    if hsdata['close'][-1]>malast[-1]:
        return rs_const.C_POSITON_MA_STATUS['_ON_MA']
    else:
        return rs_const.C_POSITON_MA_STATUS['_BLOW_MA']
def _append_whichday_freq_close(contract, startdate=datetime.today().date(), enddate=datetime.today().date(),freq='60m'):
    """
    获得当日当前周期所有收盘价
    :param contract:
    :param startdate:
    :param enddate:
    :param freq:
    :return:
    """
    dateserize=pd.date_range('2018-10-01 10:00:00', periods=30, freq='3600s')
    hsdata = get_price(rs_const.AllCONTRACTS_MAIN[contract], start_date=startdate, end_date=enddate, frequency=freq,
                       skip_paused=True)
    print(hsdata.index.hour())
    #if(hour>15)
def _check_whichday_freq_is_all_in_json(checkdate,freq):
    """

    :param checkdate:
    :param freq:
    :return:
    """
def _count_all_contracts_flow():#计算所有主要合约当日涨幅
    print('_count')
def _count_big_contracts_bigflow():#计算主要合约涨跌幅超过3%的数量
    print('count')
def _count_contracts_newhigh(nday):#计算n日内创新高/新低数量
    print('')