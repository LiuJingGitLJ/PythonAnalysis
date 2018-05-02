
# coding: utf-8

# # Pandas统计计算和描述

# In[1]:


import numpy as np
import pandas as pd


# * 常用的统计计算

# In[2]:


df_obj = pd.DataFrame(np.random.randn(5,4), columns = ['a', 'b', 'c', 'd'])
df_obj


# In[3]:


df_obj.sum()


# In[4]:


df_obj.max()


# In[5]:


df_obj.min(axis=1)


# * 统计描述

# In[6]:


df_obj.describe()

