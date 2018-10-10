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
from wxpy import *
from rstrade.jqdata import rs_fut_const as rs_const

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
    hsdata = get_price(rs_const.BLACK_MAIN[contracts], start_date=startdate, end_date=endday, frequency=freq,
                       skip_paused=True)
    data_len = range(len(hsdata))
    base_price = hsdata['close'][0]
    plt.plot(data_len, hsdata['close'] / base_price, rs_const.BLACK_LINECOLOR[contracts], label=contracts)
    return


auth('15916406969','a456789')#依次输入账号、密码，链接到平台数据库

startdate='2018-07-27'
freq='1d'
endday = datetime.date.today()

plt.figure()

_join_contracts('MA',startdate,endday,freq)
_join_contracts('RB',startdate,endday,freq)
_join_contracts('HC',startdate,endday,freq)
_join_contracts('J',startdate,endday,freq)
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

bot =Bot(cache_path=True)
#bot.file_helper.send("hello")
def sendNews():
    t = Timer(30, bot.file_helper.send("hello"))
    t.start()
sendNews()
if __name__ == "__main__":
    sendNews()


