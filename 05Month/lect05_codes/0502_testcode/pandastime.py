# coding: utf-8

from datetime import datetime
import pandas as pd
import numpy as np

#指定index 为datetime的list

date_list = [datetime(2017, 2, 18), datetime(2017, 2, 19),
             datetime(2017, 2, 25),datetime(2017, 2, 27),
             datetime(2017, 3, 4),datetime(2017, 3, 5)]
time_s = pd.Series(np.random.randn(6), index=date_list)

print(time_s)

print(date_list)

print(time_s.index)


# 起始日期 周期 频率
dates = pd.date_range('2017-02-18', periods=10, freq='W-SAT')

print(dates)

print(pd.Series(np.random.randn(5), index=dates))