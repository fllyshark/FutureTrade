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

def _join_contracts(contracts, startdate, endday, freq):
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
    hsdata = get_price(rs_const.CONTRACTS_MAIN[contracts], start_date=startdate, end_date=endday, frequency=freq,
                       skip_paused=True)
    data_len = range(len(hsdata))
    if len(hsdata)<=0:
        print("%s--该合约无数据！exit--\n"%rs_const.CONTRACTS_MAIN[contracts])
        return
    base_price = hsdata['close'][0]
    #plt.plot(data_len, hsdata['close'] / base_price, rs_const.BLACK_LINECOLOR[contracts], label=contracts)
    plt.plot(data_len, hsdata['close'] / base_price, label=contracts)
    malast=indi.ma(hsdata,50)

    if hsdata['close'][-1]>malast[-1]:
       strclc=("%s收盘价大于50周期线\n"%contracts)
       #print(rs_const.FILEPATH['clc_file'])
       fileu.appendStrToFile(rs_const.clc_filepath%(datetime.date.today().strftime('%Y-%m-%d')),strclc)

    return


auth('15916406969','a456789')#依次输入账号、密码，链接到平台数据库

startdate='2018-05-27'
freq='1d'
endday = datetime.date.today()

plt.figure(figsize=(9, 9.5))

#_join_contracts('MA',startdate,endday,freq)
#_join_contracts('RB',startdate,endday,freq)
#_join_contracts('HC',startdate,endday,freq)
#_join_contracts('J',startdate,endday,freq)
for index in rs_const.CONTRACTS_MAIN:
    _join_contracts(index, startdate, endday, freq)
#plt.text(4, 5, 6, ha='center', va='bottom', fontsize=20)

plt.title("future line")

plt.xlabel("clc")
plt.ylabel("price")
#设置x坐标轴刻度
#my_x_ticks = np.arange(0, len(rb_hsdata), 1)
#plt.xticks(my_x_ticks)


plt.grid(True)
plt.legend(loc=1,ncol=2)

plt.show()



