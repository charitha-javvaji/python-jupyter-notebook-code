#!/usr/bin/env python
# coding: utf-8

# In[69]:


a = [1,2,5,7,8,10]
b = [3,4,7,9,10,11]

x=[]

for i in range(0,len(a)):
    if i==0:
        if a[i]<b[i]:
            x.append(b)
    
    elif i < len(b):
        if b[(i-1)]<=a[i]:
            if b[i]:
                x.append(a)
print('number of intervals ', len(x))


# In[ ]:




