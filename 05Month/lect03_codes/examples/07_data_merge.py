
# coding: utf-8

# # 数据连接 merge

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


df_obj1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                        'data1' : np.random.randint(0,10,7)})
df_obj2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                        'data2' : np.random.randint(0,10,3)})

print(df_obj1)
print(df_obj2)


# In[4]:


# 默认将重叠列的列名作为“外键”进行连接
pd.merge(df_obj1, df_obj2)


# In[5]:


# on显示指定“外键”
pd.merge(df_obj1, df_obj2, on='key')


# In[6]:


# left_on，right_on分别指定左侧数据和右侧数据的“外键”

# 更改列名
df_obj1 = df_obj1.rename(columns={'key':'key1'})
df_obj2 = df_obj2.rename(columns={'key':'key2'})


# In[7]:


pd.merge(df_obj1, df_obj2, left_on='key1', right_on='key2')


# In[8]:


# “外连接”
pd.merge(df_obj1, df_obj2, left_on='key1', right_on='key2', how='outer')


# In[9]:


# 左连接
pd.merge(df_obj1, df_obj2, left_on='key1', right_on='key2', how='left')


# In[10]:


# 右连接
pd.merge(df_obj1, df_obj2, left_on='key1', right_on='key2', how='right')


# In[11]:


# 处理重复列名
df_obj1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                        'data' : np.random.randint(0,10,7)})
df_obj2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                        'data' : np.random.randint(0,10,3)})

pd.merge(df_obj1, df_obj2, on='key', suffixes=('_left', '_right'))


# In[12]:


# 按索引连接
df_obj1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                        'data1' : np.random.randint(0,10,7)})
df_obj2 = pd.DataFrame({'data2' : np.random.randint(0,10,3)}, index=['a', 'b', 'd'])


# In[13]:


pd.merge(df_obj1, df_obj2, left_on='key', right_index=True)

