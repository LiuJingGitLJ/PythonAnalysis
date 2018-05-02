
# coding: utf-8

# # ARIMA模型

# ## 平稳性

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

# 构造时间时间序列
df_obj = pd.DataFrame(np.random.randn(1000, 1), 
                       index=pd.date_range('20170101', periods=1000),
                       columns=['data'])
df_obj['data'] = df_obj['data'].cumsum()
print(df_obj.head())


# In[16]:


# 一阶差分处理
df_obj['diff_1'] = df_obj['data'].diff(1)

# 二阶差分处理
df_obj['diff_2'] = df_obj['diff_1'].diff(1)

# 查看图像
df_obj.plot(subplots=True, figsize=(18, 12))


# ## ACF 和 PACF

# In[37]:


from scipy import  stats
import statsmodels.api as sm

sm.graphics.tsa.plot_acf(df_obj['data'], lags=20)
sm.graphics.tsa.plot_pacf(df_obj['data'], lags=20)

