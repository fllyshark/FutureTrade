# -*- coding:utf-8 -*-

from datetime import datetime,timedelta
import time
import pandas as pd
from jqdatasdk import *

def year_qua(date):
    mon = date[5:7]
    mon = int(mon)
    return [date[0:4], _quar(mon)]


def _quar(mon):
    if mon in [1, 2, 3]:
        return '1'
    elif mon in [4, 5, 6]:
        return '2'
    elif mon in [7, 8, 9]:
        return '3'
    elif mon in [10, 11, 12]:
        return '4'
    else:
        return None


def today():
    day = datetime.today().date()
    return str(day)


def get_year():
    year = datetime.today().year
    return year


def get_month():
    month = datetime.today().month
    return month


def get_hour():
    return datetime.today().hour


def today_last_year():
    lasty = datetime.today().date() + datetime.timedelta(-365)
    return str(lasty)


def day_last_week(days=-7):
    lasty = datetime.today().date() + datetime.timedelta(days)
    return str(lasty)


def get_now():
    return time.strftime('%Y-%m-%d %H:%M:%S')
def get_yestoday():
    yesterday = datetime.today().date() + timedelta(days=-1)
    return yesterday.strftime('%Y-%m-%d')
def get_tomorow():
    tomorow = datetime.today().date() + timedelta(days=1)
    return tomorow.strftime('%Y-%m-%d')

def int2time(timestamp):
    datearr = datetime.utcfromtimestamp(timestamp)
    timestr = datearr.strftime("%Y-%m-%d %H:%M:%S")
    return timestr


def diff_day(start=None, end=None):
    d1 = datetime.strptime(end, '%Y-%m-%d')
    d2 = datetime.strptime(start, '%Y-%m-%d')
    delta = d1 - d2
    return delta.days


def get_quarts(start, end):
    idx = pd.period_range('Q'.join(year_qua(start)), 'Q'.join(year_qua(end)),
                          freq='Q-JAN')
    return [str(d).split('Q') for d in idx][::-1]


def is_trade_date():
    '''
            交易日历
    isOpen=1是交易日，isOpen=0为休市
    '''
    np_date = get_trade_days(count=1)
    if(np_date[0] ==datetime.date.today()):
        return True
    else:
        return False




def last_tddate():
    today = datetime.today().date()
    today = int(today.strftime("%w"))
    if today == 0:
        return day_last_week(-2)
    else:
        return day_last_week(-1)


def tt_dates(start='', end=''):
    startyear = int(start[0:4])
    endyear = int(end[0:4])
    dates = [d for d in range(startyear, endyear + 1, 2)]
    return dates


def _random(n=13):
    from random import randint
    start = 10 ** (n - 1)
    end = (10 ** n) - 1
    return str(randint(start, end))


def get_q_date(year=None, quarter=None):
    dt = {'1': '-03-31', '2': '-06-30', '3': '-09-30', '4': '-12-31'}
    return '%s%s' % (str(year), dt[str(quarter)])

