
# coding: utf-8

# # Seaborn

# In[1]:


import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')


# * 数据集分布可视化

# In[2]:


# 单变量分布
x1 = np.random.normal(size=1000)
sns.distplot(x1);


# In[3]:


x2 = np.random.randint(0, 100, 500)
sns.distplot(x2);


# In[4]:


# 直方图
sns.distplot(x1, bins=20, kde=False, rug=True)


# In[5]:


# 核密度估计
sns.distplot(x2, hist=False, rug=True)


# In[6]:


sns.kdeplot(x2, shade=True)
sns.rugplot(x2)


# In[7]:


# 拟合参数分布
sns.distplot(x1, kde=False, fit=stats.gamma)


# In[8]:


# 双变量分布
df_obj1 = pd.DataFrame({"x": np.random.randn(500),
                   "y": np.random.randn(500)})

df_obj2 = pd.DataFrame({"x": np.random.randn(500),
                   "y": np.random.randint(0, 100, 500)})


# In[9]:


# 散布图
sns.jointplot(x="x", y="y", data=df_obj1)


# In[10]:


# 二维直方图
sns.jointplot(x="x", y="y", data=df_obj1, kind="hex");


# In[11]:


# 核密度估计
sns.jointplot(x="x", y="y", data=df_obj1, kind="kde");


# In[12]:


# 数据集中变量间关系可视化
dataset = sns.load_dataset("tips")
#dataset = sns.load_dataset("iris")
sns.pairplot(dataset);


# # 类别数据可视化

# In[13]:


#titanic = sns.load_dataset('titanic')
#planets = sns.load_dataset('planets')
#flights = sns.load_dataset('flights')
#iris = sns.load_dataset('iris')
exercise = sns.load_dataset('exercise')


# * 类别散布图

# In[14]:


sns.stripplot(x="diet", y="pulse", data=exercise)


# In[15]:


sns.swarmplot(x="diet", y="pulse", data=exercise, hue='kind')


# * 类别内数据分布

# In[16]:


# 盒子图
sns.boxplot(x="diet", y="pulse", data=exercise)
#sns.boxplot(x="diet", y="pulse", data=exercise, hue='kind')


# In[17]:


# 小提琴图
#sns.violinplot(x="diet", y="pulse", data=exercise)
sns.violinplot(x="diet", y="pulse", data=exercise, hue='kind')


# * 类别内统计图

# In[18]:


# 柱状图
sns.barplot(x="diet", y="pulse", data=exercise, hue='kind')


# In[19]:


# 点图
sns.pointplot(x="diet", y="pulse", data=exercise, hue='kind');

