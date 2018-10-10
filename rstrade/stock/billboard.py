#!/usr/bin/python3
"""
# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 18:04
# @Author  : wly
# @Email   : 787115719@qq.com
# @File    : billboard.py
# @Software: PyCharm
"""
import pandas as pd
from pandas.compat import StringIO
from rstrade.stock import rs_const as rs_c
import numpy as np
import time
import re
import lxml.html
from lxml import etree
from rstrade.stock import rs_varurl as rs_url
from rstrade.stock import rs_util_function as rs_func

"""版本兼容问题 urllib.request 在高版本python中才有，如果找不到，则用urllib2 """
from urllib.request import urlopen, Request




def cap_tops(days=5, retry_count=3, pause=0.001):
    """
    获取个股上榜统计数据
    Parameters
    --------
        days:int
                  天数，统计n天以来上榜次数，默认为5天，其余是10、30、60
        retry_count : int, 默认 3
                     如遇网络等问题重复执行的次数
        pause : int, 默认 0
                    重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    Return
    ------
    DataFrame
        code：代码
        name：名称
        count：上榜次数
        bamount：累积购买额(万)
        samount：累积卖出额(万)
        net：净额(万)
        bcount：买入席位数
        scount：卖出席位数
    """

    if rs_func._check_cyclical_input(days) is True:
        rs_func._write_waiting_tips_head()
        df = _cap_tops(days, pageNo=1, retry_count=retry_count,
                       pause=pause)
        rs_func._write_other_line()
        df['code'] = df['code'].map(lambda x: str(x).zfill(6))

        if df is not None:
            df = df.drop_duplicates('code')
        return df


def _cap_tops(last=5, pageNo=1, retry_count=3, pause=0.001, dataArr=pd.DataFrame()):
    rs_func._write_wait_flag()
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            request = Request(rs_url.URL_SINA_LHB % ( rs_c.DOMAINS['vipsina'], rs_url.VAR_SINA_KINDS_COLS[0],
                                                 rs_url.VAR_END_PAGES['fd'], last, pageNo))
            text = urlopen(request, timeout=10).read()
            text = text.decode('GBK')
            html = lxml.html.parse(StringIO(text))
            res = html.xpath("//table[@id=\"dataTable\"]/tr")
            if rs_c.PY3:
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
            else:
                sarr = [etree.tostring(node) for node in res]
            sarr = ''.join(sarr)
            sarr = '<table>%s</table>' % sarr
            df = pd.read_html(sarr)[0]
            df.columns = rs_url.VAR_SINA_GGTJ_COLS
            dataArr = dataArr.append(df, ignore_index=True)
            nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')
            if len(nextPage) > 0:
                pageNo = re.findall(r'\d+', nextPage[0])[0]
                return _cap_tops(last, pageNo, retry_count, pause, dataArr)
            else:
                return dataArr
        except Exception as e:
            print(e)


def broker_tops(days=5, retry_count=3, pause=0.001):
    """
    获取营业部上榜统计数据
    Parameters
    --------
    days:int
              天数，统计n天以来上榜次数，默认为5天，其余是10、30、60
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    Return
    ---------
    broker：营业部名称
    count：上榜次数
    bamount：累积购买额(万)
    bcount：买入席位数
    samount：累积卖出额(万)
    scount：卖出席位数
    top3：买入前三股票
    """
    if ct._check_lhb_input(days) is True:
        ct._write_head()
        df = _broker_tops(days, pageNo=1, retry_count=retry_count,
                          pause=pause)
        return df


def _broker_tops(last=5, pageNo=1, retry_count=3, pause=0.001, dataArr=pd.DataFrame()):
    ct._write_console()
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            request = Request(rv.LHB_SINA_URL % (ct.P_TYPE['http'], ct.DOMAINS['vsf'], rv.LHB_KINDS[1],
                                                 ct.PAGES['fd'], last, pageNo))
            text = urlopen(request, timeout=10).read()
            text = text.decode('GBK')
            html = lxml.html.parse(StringIO(text))
            res = html.xpath("//table[@id=\"dataTable\"]/tr")
            if ct.PY3:
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
            else:
                sarr = [etree.tostring(node) for node in res]
            sarr = ''.join(sarr)
            sarr = '<table>%s</table>' % sarr
            df = pd.read_html(sarr)[0]
            df.columns = rv.LHB_YYTJ_COLS
            dataArr = dataArr.append(df, ignore_index=True)
            nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')
            if len(nextPage) > 0:
                pageNo = re.findall(r'\d+', nextPage[0])[0]
                return _broker_tops(last, pageNo, retry_count, pause, dataArr)
            else:
                return dataArr
        except Exception as e:
            print(e)


def inst_tops(days=5, retry_count=3, pause=0.001):
    """
    获取机构席位追踪统计数据
    Parameters
    --------
    days:int
              天数，统计n天以来上榜次数，默认为5天，其余是10、30、60
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题

    Return
    --------
    code:代码
    name:名称
    bamount:累积买入额(万)
    bcount:买入次数
    samount:累积卖出额(万)
    scount:卖出次数
    net:净额(万)
    """
    if ct._check_lhb_input(days) is True:
        ct._write_head()
        df = _inst_tops(days, pageNo=1, retry_count=retry_count,
                        pause=pause)
        df['code'] = df['code'].map(lambda x: str(x).zfill(6))
        return df


def _inst_tops(last=5, pageNo=1, retry_count=3, pause=0.001, dataArr=pd.DataFrame()):
    ct._write_console()
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            request = Request(rv.LHB_SINA_URL % (ct.P_TYPE['http'], ct.DOMAINS['vsf'], rv.LHB_KINDS[2],
                                                 ct.PAGES['fd'], last, pageNo))
            text = urlopen(request, timeout=10).read()
            text = text.decode('GBK')
            html = lxml.html.parse(StringIO(text))
            res = html.xpath("//table[@id=\"dataTable\"]/tr")
            if ct.PY3:
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
            else:
                sarr = [etree.tostring(node) for node in res]
            sarr = ''.join(sarr)
            sarr = '<table>%s</table>' % sarr
            df = pd.read_html(sarr)[0]
            df = df.drop([2, 3], axis=1)
            df.columns = rv.LHB_JGZZ_COLS
            dataArr = dataArr.append(df, ignore_index=True)
            nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')
            if len(nextPage) > 0:
                pageNo = re.findall(r'\d+', nextPage[0])[0]
                return _inst_tops(last, pageNo, retry_count, pause, dataArr)
            else:
                return dataArr
        except Exception as e:
            print(e)


def inst_detail(retry_count=3, pause=0.001):
    """
    获取最近一个交易日机构席位成交明细统计数据
    Parameters
    --------
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数
    pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题

    Return
    ----------
    code:股票代码
    name:股票名称
    date:交易日期
    bamount:机构席位买入额(万)
    samount:机构席位卖出额(万)
    type:类型
    """
    ct._write_head()
    df = _inst_detail(pageNo=1, retry_count=retry_count,
                      pause=pause)
    if len(df) > 0:
        df['code'] = df['code'].map(lambda x: str(x).zfill(6))
    return df


def _inst_detail(pageNo=1, retry_count=3, pause=0.001, dataArr=pd.DataFrame()):
    ct._write_console()
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            request = Request(rv.LHB_SINA_URL % (ct.P_TYPE['http'], ct.DOMAINS['vsf'], rv.LHB_KINDS[3],
                                                 ct.PAGES['fd'], '', pageNo))
            """
            wangdf test
            """
            print(rv.LHB_SINA_URL % (ct.P_TYPE['http'], ct.DOMAINS['vsf'], rv.LHB_KINDS[3],
                                     ct.PAGES['fd'], '', pageNo))
            text = urlopen(request, timeout=10).read()
            text = text.decode('GBK')
            html = lxml.html.parse(StringIO(text))
            res = html.xpath("//table[@id=\"dataTable\"]/tr")
            if ct.PY3:
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
            else:
                sarr = [etree.tostring(node) for node in res]
            sarr = ''.join(sarr)
            sarr = '<table>%s</table>' % sarr
            df = pd.read_html(sarr)[0]
            df.columns = rv.LHB_JGMX_COLS
            dataArr = dataArr.append(df, ignore_index=True)
            nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')
            if len(nextPage) > 0:
                pageNo = re.findall(r'\d+', nextPage[0])[0]
                return _inst_detail(pageNo, retry_count, pause, dataArr)
            else:
                return dataArr
        except Exception as e:
            print(e)


def _f_rows(x):
    if '%' in x[3]:
        x[11] = x[6]
        for i in range(6, 11):
            x[i] = x[i - 5]
        for i in range(1, 6):
            x[i] = np.NaN
    return x
