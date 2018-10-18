#!/usr/bin/python3
"""
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 11:38
# @Author  : wly
# @Email   : 787115719@qq.com
# @File    : plt_ma_count.py
# @Software: PyCharm
"""
import matplotlib.pyplot as plt
from rstrade.jqdata import alpha_trend as atrend
def plt_ma_count(contracts,startdate,endday,freq,which_ma):
    """

    :param contracts:
    :param startdate:
    :param endday:
    :param freq:
    :param which_ma:
    :return:
    """
    dic=atrend._get_count_contracts_number(contracts,startdate,endday,freq,which_ma)
    plt.figure()
    plt.ylim(-150,150)
    t=0
    lis=[]
    for key in dic.keys():
        if len(dic[key])>t:
            t=len(dic[key])
    for key in dic.keys():
        xzhou=dic[key][1]
        yzhou=0
        if dic[key][0]==2:
            yzhou=dic[key][1]*-1
        else:
            yzhou=dic[key][1]
        plt.plot([xzhou,xzhou],[0,yzhou],label=key)
        plt.text(xzhou, yzhou, key+':'+str(yzhou), ha='center', va='bottom', fontsize=9)
    plt.xlabel("周期数")
    plt.ylabel("之上数")

    plt.grid(True)
    plt.legend(loc=1, ncol=2)
    plt.show()