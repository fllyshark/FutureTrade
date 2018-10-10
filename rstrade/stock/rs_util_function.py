#!/usr/bin/python3
"""
# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 22:38
# @Author  : wly
# @Email   : 787115719@qq.com
# @File    : rs_util_function.py
# @Software: PyCharm
"""

import  sys

ERROR_CR_MSG = '周期输入有误，请输入数字5、10、30或60'

WAIT_DATA_TIPS = '[Getting URL data,please wait:]'
DATA_GETTING_FLAG = '#'

def _check_cyclical_input(last):
    """
    周期校检
    :param last:输入周期
    :return:
    """
    if last not in [5, 10, 30, 60]:
        raise TypeError(ERROR_CR_MSG)
    else:
        return True

def _write_waiting_tips_head():
    """
    网络请求等待提示
    :return:
    """
    sys.stdout.write(WAIT_DATA_TIPS)
    sys.stdout.flush()
def _write_wait_flag():
    """
    网络请求中，打印等待符号
    :return:
    """
    sys.stdout.write(DATA_GETTING_FLAG)
    sys.stdout.flush()
def _write_other_line():
    """
    换行
    :return:
    """
    sys.stdout.write("\n")
    sys.stdout.flush()