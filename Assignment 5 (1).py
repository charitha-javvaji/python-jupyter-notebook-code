#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Imported pandas and numpy


# In[1]:


import pandas as pd
import numpy as np


# In[2]:


read=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")


# In[3]:


# To read the data


# In[4]:


read


# In[5]:


# To check the null-values


# In[6]:


read.isnull().sum()


# In[7]:


# To Drop the ccolumn


# In[8]:


read.drop(['Cabin'],axis=1)


# In[9]:


# Replace NaN values with Mean


# In[10]:


read['Age']=read['Age'].fillna(np.mean(read['Age']))


# In[11]:


read


# In[12]:


# To describe the data


# In[13]:


read.describe()


# In[14]:


# To check the data type


# In[15]:


read.info()


# In[16]:


# To  rename the columns


# In[17]:


rename=read.rename({'Sex':'Gender','Name':'Full Name'},axis=1)


# In[18]:


rename


# In[19]:


# Total male 


# In[30]:


total_males=rename[(rename['Gender']=='male')]


# In[31]:


total_males


# In[ ]:


# Total female


# In[32]:


total_females=rename[(rename['Gender']=='female')]


# In[33]:


total_females


# In[ ]:


# Male survived in titanic ship


# In[38]:


male=rename[(rename['Gender']=='male') & rename['Survived']==1]


# In[39]:


male                                                                        


# In[40]:


# Female survived in titanic ship


# In[41]:


female=rename[(rename['Gender']=='female') & rename['Survived']==1]


# In[42]:


female


# In[43]:


# Total rich people 


# In[44]:


ac1=rename[(rename['Fare']>25) ]


# In[45]:


ac1


# In[46]:


# Total poor people


# In[47]:


ac2=rename[(rename['Fare']<25)]


# In[48]:


ac2


# In[49]:


# Total rich females survived 


# In[50]:


df1=rename[(rename['Fare']>25) & (rename['Gender']=='female') & rename['Survived']==1]


# In[51]:


df1


# In[52]:


#Total rich males survived


# In[53]:


df2=rename[(rename['Fare']>25) & (rename['Gender']=='male') & rename['Survived']==1]


# In[54]:


df2


# In[55]:


# To getting count of rows


# In[56]:


df2.Survived.count()


# In[57]:


df1.Survived.count()


# In[58]:


total_males.Gender.count()


# In[92]:


total_females.Gender.count()


# In[62]:


rename.Gender.count()


# In[63]:


male.Gender.count()


# In[64]:


female.Gender.count()


# In[65]:


ac1.Fare.count()


# In[66]:


ac2.Fare.count()


# In[ ]:


# Percentages


# In[86]:


A=(df1.Survived.count()/ac1.Fare.count())*100 


# In[87]:


A


# In[93]:


A.round()


# In[73]:


(df2.Survived.count()/ac1.Fare.count())*100


# In[71]:


(male.Gender.count()/total_males.Gender.count())*100


# In[72]:


(female.Gender.count()/total_females.Gender.count())*100


# In[ ]:


# Final result


# In[ ]:


# Total male = 577, Female = 314

# Male survived = 109, Female survived = 233, 

# % for male survived = 18.890, % for female survived = 74.20

# Total rich members = 334, Total poor members = 557

# % male rich people survived = 17.36, % female rich people survived = 37.12

