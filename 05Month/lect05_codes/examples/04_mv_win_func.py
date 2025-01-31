
# coding: utf-8

# # 时间序列数据统计—滑动窗口

# ## 窗口函数

# In[15]:


import pandas as pd
import numpy as np

ser_obj = pd.Series(np.random.randn(1000), 
                    index=pd.date_range('20170101', periods=1000))
ser_obj = ser_obj.cumsum()
print(ser_obj.head())


# In[16]:


print(ser_obj.head())


# In[17]:


r_obj = ser_obj.rolling(window=5)
print(r_obj)


# In[18]:


print(r_obj.mean())

# 验证：
# 前5个数据的均值
# print(ser_obj[0:5].mean())

# 1-6个数据的均值
# print(ser_obj[1:6].mean())


# In[26]:


# 画图查看
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.figure(figsize=(15, 5))

ser_obj.plot(style='r--')
ser_obj.rolling(window=10).mean().plot(style='b')


# In[29]:


print(ser_obj.rolling(window=5, center=True).mean())

