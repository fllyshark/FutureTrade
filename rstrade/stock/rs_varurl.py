#!/usr/bin/python3
"""
# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 22:24
# @Author  : wly
# @Email   : 787115719@qq.com
# @File    : rs_varurl.py
# @Software: PyCharm
"""
"""
网络地址公共页写法汇总
"""
VAR_END_PAGES = {'fd': 'index.phtml', 'dl': 'downxls.php', 'jv': 'json_v2.php',
         'cpt': 'newFLJK.php', 'ids': 'newSinaHy.php', 'lnews': 'rollnews_ch_out_interface.php',
         'ntinfo': 'vCB_BulletinGather.php', 'hs300b': '000300cons.xls',
         'hs300w': '000300closeweight.xls', 'sz50b': '000016cons.xls',
         'dp': 'all_fpya.php', '163dp': 'fpyg.html',
         'emxsg': 'JS.aspx', '163fh': 'jjcgph.php',
         'newstock': 'vRPD_NewStockIssue.php', 'zz500b': '000905cons.xls',
         'zz500wt': '000905closeweight.xls',
         't_ticks': 'vMS_tradedetail.php', 'dw': 'downLoad.html',
         'qmd': 'queryMargin.do', 'szsefc': 'ShowReport.szse',
         'ssecq': 'commonQuery.do', 'sinadd': 'cn_bill_download.php'}

"""
新浪网络数据地址
"""
URL_SINA_LHB = '%s/q/go.php/vLHBData/kind/%s/%s?last=%s&p=%s'
VAR_SINA_GGTJ_COLS = ['code', 'name', 'count', 'bamount', 'samount', 'net', 'bcount', 'scount']
VAR_SINA_KINDS_COLS = ['ggtj', 'yytj', 'jgzz', 'jgmx']

