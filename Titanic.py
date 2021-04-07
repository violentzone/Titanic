#!/usr/bin/env python
# coding: utf-8

# # Titanic Project
# ## EDA

# In[1]:


#import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.model_selection import train_test_split


# In[2]:


#import data of titanic train
data = pd.read_csv('D://Python/titanic/train.csv')
data.head()


# #### 12 columns, Survived as the training anser

# ## Start EDA

# In[5]:


data.count()


# #### Missing values in Age, Cabin and Embarked
# #### PassengerId inrelevent

# In[6]:


data1 = data.drop("PassengerId", axis=1)


# #### Pcalss:

# In[7]:


data1['Pclass'].value_counts()


# In[8]:


#Pclass is already grouped, check death rate in each class
death = 


# In[ ]:




