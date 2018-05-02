
# coding: utf-8

# # Pandas数据操作

# In[1]:


import pandas as pd


# * Series索引

# In[2]:


ser_obj = pd.Series(range(5), index = ['a', 'b', 'c', 'd', 'e'])
print(ser_obj.head())


# In[3]:


# 行索引
print(ser_obj['a'])
print(ser_obj[0])


# In[4]:


# 切片索引
print(ser_obj[1:3])
print(ser_obj['b':'d'])


# In[5]:


# 不连续索引
print(ser_obj[[0, 2, 4]])
print(ser_obj[['a', 'e']])


# In[6]:


# 布尔索引
ser_bool = ser_obj > 2
print(ser_bool)
print(ser_obj[ser_bool])

print(ser_obj[ser_obj > 2])


# * DataFrame索引

# In[7]:


import numpy as np

df_obj = pd.DataFrame(np.random.randn(5,4), columns = ['a', 'b', 'c', 'd'])
print(df_obj.head())


# In[8]:


# 列索引
print('列索引')
print(df_obj['a']) # 返回Series类型
print(type(df_obj[[0]])) # 返回DataFrame类型

# 不连续索引
print('不连续索引')
print(df_obj[['a','c']])
print(df_obj[[1, 3]])


# * 三种索引方式

# In[9]:


# 标签索引 loc
# Series
print(ser_obj['b':'d'])
print(ser_obj.loc['b':'d'])

# DataFrame
print(df_obj['a'])
print(df_obj.loc[0:2, 'a'])


# In[10]:


# 整型位置索引 iloc
print(ser_obj[1:3])
print(ser_obj.iloc[1:3])

# DataFrame
print(df_obj.iloc[0:2, 0]) # 注意和df_obj.loc[0:2, 'a']的区别


# In[11]:


# 混合索引 ix
print(ser_obj.ix[1:3])
print(ser_obj.ix['b':'c'])

# DataFrame
print(df_obj.ix[0:2, 0]) # 先按标签索引尝试操作，然后再按位置索引尝试操作


# * 运算与对齐

# In[12]:


s1 = pd.Series(range(10, 20), index = range(10))
s2 = pd.Series(range(20, 25), index = range(5))

print('s1: ' )
print(s1)

print('') 

print('s2: ')
print(s2)


# In[13]:


# Series 对齐运算
s1 + s2


# In[14]:


import numpy as np

df1 = pd.DataFrame(np.ones((2,2)), columns = ['a', 'b'])
df2 = pd.DataFrame(np.ones((3,3)), columns = ['a', 'b', 'c'])

print('df1: ')
print(df1)

print('') 
print('df2: ')
print(df2)


# In[15]:


# DataFrame对齐操作
df1 + df2


# In[16]:


# 填充未对齐的数据进行运算
print(s1)
print(s2)

s1.add(s2, fill_value = -1)


# In[17]:


df1.sub(df2, fill_value = 2.)


# In[18]:


# 填充NaN
s3 = s1 + s2
print(s3)


# In[19]:


s3_filled = s3.fillna(-1)
print(s3_filled)


# In[20]:


df3 = df1 + df2
print(df3)


# In[21]:


df3.fillna(100, inplace = True)
print(df3)


# * 函数应用

# In[22]:


# Numpy ufunc 函数
df = pd.DataFrame(np.random.randn(5,4) - 1)
print(df)

print(np.abs(df))


# In[23]:


# 使用apply应用行或列数据
#f = lambda x : x.max()
print(df.apply(lambda x : x.max()))


# In[24]:


# 指定轴方向
print(df.apply(lambda x : x.max(), axis=1))


# In[25]:


# 使用applymap应用到每个数据
f2 = lambda x : '%.2f' % x
print(df.applymap(f2))


# * 排序

# In[26]:


s4 = pd.Series(range(10, 15), index = np.random.randint(5, size=5))
print(s4)


# In[27]:


# 索引排序
s4.sort_index()


# In[28]:


df4 = pd.DataFrame(np.random.randn(3, 4), 
                   index=np.random.randint(3, size=3),
                   columns=np.random.randint(4, size=4))
print(df4)


# In[29]:


#df4.sort_index(ascending=False)
df4.sort_index(axis=1)


# In[30]:


# 按值排序
df4.sort_values(by=1)


# * 处理缺失数据

# In[31]:


df_data = pd.DataFrame([np.random.randn(3), [1., np.nan, np.nan],
                       [4., np.nan, np.nan], [1., np.nan, 2.]])
df_data.head()


# In[32]:


# isnull
df_data.isnull()


# In[33]:


# dropna
df_data.dropna()
#df_data.dropna(axis=1)


# In[34]:


# fillna
df_data.fillna(-100.)

