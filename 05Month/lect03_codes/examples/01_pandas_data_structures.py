
# coding: utf-8

# # Pandas数据结构

# In[ ]:


import pandas as pd


# * Series

# In[ ]:


# 通过list构建Series
ser_obj = pd.Series(range(10, 20))
print(type(ser_obj))


# In[ ]:


# 获取数据
print(ser_obj.values)

# 获取索引
print(ser_obj.index)


# In[ ]:


# 预览数据
print(ser_obj.head(3))


# In[ ]:


print(ser_obj)


# In[ ]:


#通过索引获取数据
print(ser_obj[0])
print(ser_obj[8])


# In[ ]:


# 索引与数据的对应关系仍保持在数组运算的结果中
print(ser_obj * 2)
print(ser_obj > 15)


# In[ ]:


# 通过dict构建Series
year_data = {2001: 17.8, 2002: 20.1, 2003: 16.5}
ser_obj2 = pd.Series(year_data)
print(ser_obj2.head())
print(ser_obj2.index)


# In[ ]:


# name属性
ser_obj2.name = 'temp'
ser_obj2.index.name = 'year'
print(ser_obj2.head())


# * DataFrame

# In[ ]:


import numpy as np

# 通过ndarray构建DataFrame
array = np.random.randn(5,4)
print(array)

df_obj = pd.DataFrame(array)
print(df_obj.head())


# In[ ]:


# 通过dict构建DataFrame
dict_data = {'A': 1., 
             'B': pd.Timestamp('20161217'),
             'C': pd.Series(1, index=list(range(4)),dtype='float32'),
             'D': np.array([3] * 4,dtype='int32'),
             'E' : pd.Categorical(["Python","Java","C++","C#"]),
             'F' : 'ChinaHadoop' }
#print dict_data
df_obj2 = pd.DataFrame(dict_data)
print(df_obj2.head())


# In[ ]:


# 通过列索引获取列数据
print(df_obj2['A'])
print(type(df_obj2['A']))

print(df_obj2.A)


# In[ ]:


# 增加列
df_obj2['G'] = df_obj2['D'] + 4
print(df_obj2.head())


# In[ ]:


# 删除列
del(df_obj2['G'] )
print(df_obj2.head())


# * 索引对象 Index

# In[ ]:


print(type(ser_obj.index))
print(type(df_obj2.index))

print(df_obj2.index)


# In[ ]:


# 索引对象不可变
df_obj2.index[0] = 2

