#!/usr/bin/env python
# coding: utf-8

# uses some Ipython syntax   https://ipython.readthedocs.io/en/stable/interactive/python-ipython-diff.html
# ## Numpy functions

# In[ ]:


import numpy as np


# In[ ]:


a=np.array([1,2,3])
type(a)
a


# In[ ]:


a=np.array([[1,2,3],[4,5,6],[7,8,9]])
a


# In[ ]:


a[2]


# In[ ]:


data1=[[1,2,3,4], [5,6,7,8]]
arr2=np.array(data1)
arr2


# In[ ]:


a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
np.add(a,b) #a+b does the same


# In[ ]:


arr2.ndim


# In[ ]:


arr2.shape


# # Extra Examples

# In[ ]:


data=np.random.randn(2,3)
data


# In[ ]:


data+data


# In[ ]:


data *10


# In[ ]:


data.dtype


# In[ ]:


data[0,1]


# ## SciPy Function

# In[ ]:


import scipy
from scipy import linalg
mat=np.array([[8,2],[1,4]])
linalg.det(mat)


# In[ ]:


linalg.lu(mat)


# ### SciPy Function - Special Functions of SciPy

# In[ ]:


from scipy import special


# In[ ]:


special.gamma(mat)


# In[ ]:


special.gammaln(mat)


# In[ ]:


special.erf(mat)


# ## Matplot Function

# In[4]:


import matplotlib.pyplot as plt
plt.plot([2,3,4,5])


# In[5]:


plt.plot([1,2,3],[2,4,9],linewidth=5.0)
plt.show()


# In[6]:


plt.plot([1,2,3],[2,4,9],alpha=0.5)
plt.show()


# In[7]:


plt.plot([1,2,3],[2,4,9],antialiased=True)
plt.show()


# In[10]:


plt.plot([1,2,3],[2,4,9],color='c')
plt.show()


# In[13]:


plt.plot([1,2,3],[2,4,9],dashes=[1,2,3])
plt.show()


# In[14]:


plt.plot([1,2,3],[2,4,9],linestyle=':')
plt.show()


# In[15]:


plt.plot([1,2,3],[2,4,9],marker='+')
plt.show()


# In[16]:


plt.plot([1,2,3],[2,4,9],marker='+',markeredgecolor='brown')
plt.show()


# In[21]:


plt.plot([1,2,3],[2,4,9],marker='+',markeredgewidth=1,markeredgecolor='brown')
plt.show()


# In[28]:


plt.plot([1,2,3],[2,4,9],marker='.',markerfacecolor='r',markersize=13.0)
plt.show()


# In[32]:


plt.plot([1,2,3],[2,4,9],color='r',zorder=1,linewidth=4)
plt.plot([1,2,6,9],[2,4,9,10],color='b',zorder=2,linewidth=4)
plt.show()


# In[37]:


plt.grid(True)
plt.plot([1,2,6,9],[2,4,9,10],zorder=2,linewidth=4)
plt.show()


# ## Pandas Function

# In[38]:


import pandas as pd


# In[39]:


stores=pd.read_csv('CPRG 109_M2stores.csv')
stores


# In[40]:


stores.columns


# In[41]:


## creating a dataframe
df=pd.DataFrame({'company':['Amazon','Apple','Google','Facebook','Microsoft'],
    'CEO':['Jeff Bezos','Tim Cook','Sundar Pichai','Mark Zuckerberg','Satya Nadella'],
    'Founded':[1994,1976,1998,2004,1975]})
df


# In[42]:


stores.TotalSales=stores.TotalSales.astype(float)
stores


# In[43]:


stores.describe()


# In[44]:


stores.groupby("Location").sum("TotalSales")


# In[45]:


# show missing values
stores.isnull()


# In[ ]:




