
# coding: utf-8

# # 数据重构

# In[1]:


import numpy as np
import pandas as pd


# * stack

# In[2]:


df_obj = pd.DataFrame(np.random.randint(0,10, (5,2)), columns=['data1', 'data2'])
df_obj

df_obj2 = pd.DataFrame(np.random.randint(0, 10, (5, 2)), columns=['data1', 'data2'])
print(df_obj2)


# In[3]:


stacked = df_obj.stack()
print(stacked)


# In[4]:


print(type(stacked))
print(type(stacked.index))


# In[5]:


# 默认操作内层索引
stacked.unstack()


# In[6]:


# 通过level指定操作索引的级别
stacked.unstack(level=0)

