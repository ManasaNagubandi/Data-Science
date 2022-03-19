#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install numpy')


# In[2]:


import numpy as np


# In[4]:


a=np.array([1,2,3])
print(a)


# In[5]:


a=np.array(1)
b=np.array([1,2,3])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,4,6]]])


# In[6]:


print(a.ndim)


# In[7]:


print(b.ndim)
print(c.ndim)
print(d.ndim)


# In[8]:


print(a.shape)


# In[9]:


print(b.shape)
print(c.shape)
print(d.shape)


# In[10]:


print(a.dtype)


# In[11]:



print(b.dtype)
print(c.dtype)
print(d.dtype)


# In[12]:


print(type(a))


# In[13]:


print(type(b))
print(type(c))
print(type(d))


# In[14]:


print(len(a))


# In[15]:


print(len(b))
print(len(c))
print(len(d))


# In[16]:


l1=[1,2,23]
l2=[1,6,6]
a1=np.array(l1)
a2=np.array(l2)


# In[17]:


print(a1)
print(a2)


# In[18]:


print(type(a1))
print(type(a2))


# In[20]:


np.arange(1,11)


# In[21]:


np.arange(1,11,3)


# In[22]:


np.eye(5,dtype=int)


# In[23]:


np.eye(5)             #default data type is float


# In[24]:


np.zeros(5)


# In[25]:


np.zeros((3,2),dtype=int)


# In[26]:


np.ones(5)


# In[27]:


np.ones((3,2),dtype=int)


# In[29]:


np.full((3,2),5)


# In[33]:


x=[1,4,9,16]
np.diag(x)


# In[35]:


np.linspace(1,10,num=2)


# In[36]:


np.linspace(1,10,num=20)


# In[37]:


np.linspace(1,10,num=5)


# In[44]:


np.random.random(1)[0]


# In[45]:


np.random.random(2)[1]


# In[46]:


np.random.random(2)[1]


# In[47]:


np.random.randn(3,2)


# In[48]:


np.random.randn(2,3)


# In[54]:


x=np.arange(1,11)
print(x)
print(x.shape)


# In[55]:


n=x.reshape(2,5)
print(n)


# In[56]:


print(x)


# In[57]:


n=x.reshape(5,2)
print(n)


# In[59]:


c=n.ravel()                  #gives original array
print(c)
print(c.shape)


# In[60]:


print(x)
x.reshape((2,5),order='F')


# In[63]:


print(x)
x.reshape(2,5)


# In[64]:


x.flatten()


# In[65]:


print(x)


# In[66]:


x[2]


# In[67]:


x[0:9:2]


# In[68]:


a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)


# In[69]:


a[2][2]


# In[70]:


a[2,2]


# In[71]:


a[-1][-1]


# In[72]:


a[-2][-2]


# In[77]:


a=np.arange(1,11)
print(a)


# In[78]:


a[0:5]


# In[79]:


a[1:5]


# In[80]:


a[1:9:2]


# In[81]:


a[::-1]


# In[82]:


a[2:]


# In[83]:


a[:2]


# In[85]:


x=np.arange(1,11)            #view
y=x
print(x)
print(y)


# In[86]:


x[0]=10
print(x)
print(y)


# In[88]:


print(np.shares_memory(x,y))
print(id(x))
print(id(y))


# In[89]:


z=np.copy(x)            #copy function
print(x)
print(z)


# In[90]:


x[0]=15
print(x)
print(z)


# In[91]:


print(np.shares_memory(x,z))


# In[95]:


a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)


# In[96]:


a>5


# In[97]:


a[a<3]


# In[100]:


a[(a>5)&(a<3)]


# In[101]:


z==x


# In[104]:


print(a)
print("\n")
print(a.transpose())


# In[105]:


a=np.array([1,2,3])
b=np.array([3,4,5])
print(a)
print(b)


# In[107]:


np.hstack((a,b))


# In[108]:


np.vstack((a,b))


# In[109]:


print(x)
print(z)


# In[110]:


np.insert(x,9,z)


# In[112]:


np.delete(x,0)


# In[113]:


print(x)           #delete is not assigned to any other variable


# In[114]:


np.sin(a)


# In[115]:


np.sin(x)


# In[116]:


np.cos(a)


# In[117]:


np.exp(a)


# In[118]:


np.sum(a)


# In[119]:


a=np.array([[1,2,3],[4,5,6]])
print(a)


# In[120]:


np.sum(a,axis=0)     #sum in row wise


# In[121]:


np.sum(a,axis=1)     #sum in cloumn wise


# In[123]:


a=np.arange(1,11)
print(a)


# In[124]:


np.mean(a)


# In[126]:


np.median(a)


# In[127]:


np.mode(a)          #mode function is not present in numpy


# In[128]:


np.std(a)


# In[129]:


np.max(a)


# In[130]:


np.sort(a)


# In[131]:


np.where(a==5)


# In[132]:


np.where(a%2==0)


# In[134]:


print(a)


# In[135]:


np.where(a<5,a,1)


# In[ ]:




