#!/usr/bin/env python
# coding: utf-8

# In[9]:


import os
import sys
import pandas as pd
from datetime import datetime


# In[10]:


def remove_bom(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
    # Remove UTF-8 BOM if it exists
    if content.startswith(b'\xef\xbb\xbf'):
        content = content[3:]
    with open(file_path, 'wb') as f:
        f.write(content)

# Clean both files before reading
remove_bom("C:/Users/Ritu/Downloads/Table_A.csv")
remove_bom("C:/Users/Ritu/Downloads/Table_B.csv")


# In[11]:


df_a=pd.read_csv("C:/Users/Ritu/Downloads/Table_A.csv", encoding='utf-8-sig')


# In[12]:


df_b=pd.read_csv("C:/Users/Ritu/Downloads/Table_B.csv", encoding='utf-8-sig')


# In[13]:


df_a.columns = df_a.columns.str.strip()


# In[14]:


df_b.columns = df_b.columns.str.strip()


# In[15]:


df_a


# In[16]:


df_b


# In[18]:


for index, row in df_a.iterrows():
    print(f"{row['StudentId']}\tA|{row['Name']}|{row['DOB']}")


# In[20]:


for index, row in df_b.iterrows():
    print(f"{row['StudentId']}\tB|{row['CourseId']}|{row['Grade']}")

