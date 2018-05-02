
# coding: utf-8

# # 分组与聚合

# * GroupBy对象

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


dict_obj = {'key1' : ['a', 'b', 'a', 'b', 
                      'a', 'b', 'a', 'a'],
            'key2' : ['one', 'one', 'two', 'three',
                      'two', 'two', 'one', 'three'],
            'data1': np.random.randn(8),
            'data2': np.random.randn(8)}
df_obj = pd.DataFrame(dict_obj)
print(df_obj)


# In[3]:


# dataframe根据key1进行分组
print(type(df_obj.groupby('key1')))


# In[4]:


# data1列根据key1进行分组
print(type(df_obj['data1'].groupby(df_obj['key1'])))


# In[4]:


# 分组运算
grouped1 = df_obj.groupby('key1')
print(grouped1.mean())

grouped2 = df_obj['data1'].groupby(df_obj['key1'])
print(grouped2.mean())


# In[5]:


# size
print(grouped1.size())
print(grouped2.size())


# In[6]:


# 按列名分组
df_obj.groupby('key1')


# In[7]:


# 按自定义key分组，列表
self_def_key = [1, 1, 2, 2, 2, 1, 1, 1]
df_obj.groupby(self_def_key).size()


# In[8]:


# 按自定义key分组，多层列表
df_obj.groupby([df_obj['key1'], df_obj['key2']]).size()


# In[9]:


# 按多个列多层分组
grouped2 = df_obj.groupby(['key1', 'key2'])
print(grouped2.size())


# In[10]:


# 多层分组按key的顺序进行
grouped3 = df_obj.groupby(['key2', 'key1'])
print(grouped3.mean())
print()
print(grouped3.mean().unstack())


# * GroupBy对象分组迭代

# In[11]:


# 单层分组
for group_name, group_data in grouped1:
    print(group_name)
    print(group_data)


# In[12]:


# 多层分组
for group_name, group_data in grouped2:
    print(group_name)
    print(group_data)


# In[13]:


# GroupBy对象转换list
list(grouped1)


# In[14]:


# GroupBy对象转换dict
dict(list(grouped1))


# In[15]:


# 按列分组
print(df_obj.dtypes)

# 按数据类型分组
df_obj.groupby(df_obj.dtypes, axis=1).size()
df_obj.groupby(df_obj.dtypes, axis=1).sum()


# * 其他分组方法

# In[16]:


df_obj2 = pd.DataFrame(np.random.randint(1, 10, (5,5)),
                       columns=['a', 'b', 'c', 'd', 'e'],
                       index=['A', 'B', 'C', 'D', 'E'])
df_obj2.ix[1, 1:4] = np.NaN
df_obj2


# In[18]:


# 通过字典分组
mapping_dict = {'a':'python', 'b':'python', 'c':'java', 'd':'C', 'e':'java'}
df_obj2.groupby(mapping_dict, axis=1).size()
df_obj2.groupby(mapping_dict, axis=1).count() # 非NaN的个数
df_obj2.groupby(mapping_dict, axis=1).sum()


# In[19]:


# 通过函数分组
df_obj3 = pd.DataFrame(np.random.randint(1, 10, (5,5)),
                       columns=['a', 'b', 'c', 'd', 'e'],
                       index=['AA', 'BBB', 'CC', 'D', 'EE'])
#df_obj3

def group_key(idx):
    """
        idx 为列索引或行索引
    """
    #return idx
    return len(idx)

df_obj3.groupby(group_key).size()

# 以上自定义函数等价于
#df_obj3.groupby(len).size()


# In[20]:


# 通过索引级别分组
columns = pd.MultiIndex.from_arrays([['Python', 'Java', 'Python', 'Java', 'Python'],
                                     ['A', 'A', 'B', 'C', 'B']], names=['language', 'index'])
df_obj4 = pd.DataFrame(np.random.randint(1, 10, (5, 5)), columns=columns)
df_obj4


# In[21]:


# 根据language进行分组
df_obj4.groupby(level='language', axis=1).sum()
df_obj4.groupby(level='index', axis=1).sum()


# * 聚合

# In[22]:


dict_obj = {'key1' : ['a', 'b', 'a', 'b', 
                      'a', 'b', 'a', 'a'],
            'key2' : ['one', 'one', 'two', 'three',
                      'two', 'two', 'one', 'three'],
            'data1': np.random.randint(1,10, 8),
            'data2': np.random.randint(1,10, 8)}
df_obj5 = pd.DataFrame(dict_obj)
print(df_obj5)


# In[23]:


# 内置的聚合函数
print(df_obj5.groupby('key1').sum())
print(df_obj5.groupby('key1').max())
print(df_obj5.groupby('key1').min())
print(df_obj5.groupby('key1').mean())
print(df_obj5.groupby('key1').size())
print(df_obj5.groupby('key1').count())
print(df_obj5.groupby('key1').describe())


# In[25]:


# 自定义聚合函数
def peak_range(df):
    """
        返回数值范围
    """
    #print type(df) #参数为索引所对应的记录
    return df.max() - df.min()

print(df_obj5.groupby('key1').agg(peak_range))
print(df_obj.groupby('key1').agg(lambda df : df.max() - df.min()))


# In[26]:


# 应用多个聚合函数

# 同时应用多个聚合函数
print(df_obj.groupby('key1').agg(['mean', 'std', 'count', peak_range])) # 默认列名为函数名


# In[27]:


print(df_obj.groupby('key1').agg(['mean', 'std', 'count', ('range', peak_range)])) # 通过元组提供新的列名


# In[28]:


# 每列作用不同的聚合函数
dict_mapping = {'data1':'mean',
                'data2':'sum'}
print(df_obj.groupby('key1').agg(dict_mapping))


# In[29]:


dict_mapping = {'data1':['mean','max'],
                'data2':'sum'}
print(df_obj.groupby('key1').agg(dict_mapping))

