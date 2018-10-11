#!/usr/bin/python3
"""
# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 15:42
# @Author  : wly
# @Email   : 787115719@qq.com
# @File    : rs_conn_jqdata.py
# @Software: PyCharm
"""
import datetime

import numpy as np
import pandas as pd
from threading import Timer
import matplotlib.pyplot as plt
import datetime
from rstrade.jqdata import rs_fut_const as rs_const
from rstrade.util import indictor as indi
from rstrade.util import fileUtils as fileu
from jqdatasdk import *


def _join_contracts_cross_ma(contracts, startdate, endday, freq):
    """
    1，获得各合约历史数据
    2,计算穿越周期线的合约
    :param contracts: 合约简写
    :param startdate: 计算开始日期
    :param endday: 计算结束日期
    :param freq: 计算周期
    :return: 'NU'--无数据、‘ON’--线上、‘BLOW’--线下
    """
    hsdata = get_price(rs_const.AllCONTRACTS_MAIN[contracts], start_date=startdate, end_date=endday, frequency=freq,
                       skip_paused=True)
    if len(hsdata)<=0:
        print("%s--该合约无数据！exit--\n"%rs_const.AllCONTRACTS_MAIN[contracts])
        return 'NU'
    malast=indi.ma(hsdata,50)
    if hsdata['close'][-1]>malast[-1]:
        return 'ON'
    else:
        return 'BLOW'
def _join_contracts_toplot(plt,contracts, startdate, endday, freq):
    """
    1，获得各合约历史数据
    2,设置基准价格
    3，划线
    :param contracts: 合约简写
    :param startdate: 计算开始日期
    :param endday: 计算结束日期
    :param freq: 计算周期
    :return:
    """
    hsdata = get_price(rs_const.AllCONTRACTS_MAIN[contracts], start_date=startdate, end_date=endday, frequency=freq,
                       skip_paused=True)
    if len(hsdata)<=0:
        print("%s--该合约无数据！exit--\n"%rs_const.AllCONTRACTS_MAIN[contracts])
        return
    base_price = hsdata['close'][0]
    data_len = range(len(hsdata))
    plt.plot(data_len, hsdata['close'] / base_price, label=contracts)
    return
def _get_countCross(contracts,startdate,endday,freq):
    """
    计算均线上下合约数
    :return:
    """
    v_count_crosson = 0
    v_count_crossblow=0
    arr_contracts_on=[]
    arr_contracts_blow=[]
    for index in contracts:
        str_stutas=_join_contracts_cross_ma(index, startdate, endday, freq)
        if str_stutas == 'ON':
            v_count_crosson=v_count_crosson+1
            arr_contracts_on.append(index)
        elif str_stutas == 'BLOW':
            v_count_crossblow=v_count_crossblow+1
            arr_contracts_blow.append(index)
    tem_filepath = rs_const.clc_filepath%(datetime.date.today().strftime('%Y-%m-%d'))
    str_to_file='线上数（多头数）：  %s\n' \
                '线下数（多头数）：  %s\n' \
                '总合约数（多头数）：%s\n'\
                %(v_count_crosson,v_count_crossblow,v_count_crosson+v_count_crossblow)

    fileu.appendStrToFile(tem_filepath,str_to_file)
    print(arr_contracts_on)
def _plt_contracts(contracts,startdate,endday,freq):
    """
        绘制涨跌幅函数：
        根据传入合约名称，绘制涨跌幅曲线
        :param contracts:
        :param startdate:计算数据开始时间
        :param endday: 计算数据结束时间
        :param freq: 周期（d，m）
        :return:
    """
    plt.figure(figsize=(9, 9.5))
    for index in contracts:
        _join_contracts_toplot(plt, index, startdate, endday, freq)
    # plt.text(4, 5, 6, ha='center', va='bottom', fontsize=20)
    plt.title("future line")

    plt.xlabel("周期数")
    plt.ylabel("涨跌幅")
    plt.grid(True)
    plt.legend(loc=1, ncol=2)
    # 设置x坐标轴刻度
    # my_x_ticks = np.arange(0, len(rb_hsdata), 1)
    # plt.xticks(my_x_ticks)
    plt.show()

auth('15916406969','a456789')#依次输入账号、密码，链接到平台数据库
startdate='2018-05-27'
freq='1d'
endday = datetime.date.today()

_get_countCross(rs_const.CONTRACTS_MAIN,startdate,endday,freq)
_plt_contracts(rs_const.WATCH_MAIN,startdate,endday,freq)



