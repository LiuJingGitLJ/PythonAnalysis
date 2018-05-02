
# coding: utf-8

# # 数据转换

# In[1]:


import numpy as np
import pandas as pd


# * 重复数据

# In[2]:


df_obj = pd.DataFrame({'data1' : ['a'] * 4 + ['b'] * 4,
                       'data2' : np.random.randint(0, 4, 8)})
df_obj


# In[3]:


df_obj.duplicated()


# In[4]:


df_obj.drop_duplicates()


# In[5]:


df_obj.drop_duplicates('data2')


# * map函数

# In[6]:


ser_obj = pd.Series(np.random.randint(0,10,10))
ser_obj


# In[7]:


ser_obj.map(lambda x : x ** 2)


# * 数据替换repalce

# In[8]:


# 替换单个值
ser_obj.replace(0, -100)


# In[9]:


# 替换多个值
ser_obj.replace([0, 2], -100)


# In[10]:


# 替换多个值
ser_obj.replace([0, 2], [-100, -200])

