
# coding: utf-8

# # Pandas层级索引

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


ser_obj = pd.Series(np.random.randn(12),
                    index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd'],
                           [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]])
print(ser_obj)


# * MultiIndex索引对象

# In[3]:


print(type(ser_obj.index))
print(ser_obj.index)


# * 选取子集

# In[4]:


# 外层选取
print(ser_obj['c'])


# In[5]:


# 内层选取
print(ser_obj[:, 2])


# * 交换分层顺序

# In[6]:


print(ser_obj.swaplevel())


# * 交换并排序分层

# In[7]:


print(ser_obj.swaplevel().sortlevel())

