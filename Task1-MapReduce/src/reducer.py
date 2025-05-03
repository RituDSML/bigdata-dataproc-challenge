#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import sys
import pandas as pd
from datetime import datetime


# In[6]:


df = pd.read_csv(r"C:\Users\Ritu\Downloads\mapper_output.txt", sep="\t", header=None, names=["StudentId", "Data"])


# In[15]:


df_a = df[df["Data"].str.startswith("A|")].copy()
df_b = df[df["Data"].str.startswith("B|")].copy()


# In[16]:


df_a[["Name", "DOB"]] = df_a["Data"].str[2:].str.split("|", expand=True)
df_a["DOB"] = df_a["DOB"].str.strip()


# In[17]:


df_b[["CourseId", "Grade"]] = df_b["Data"].str[2:].str.split("|", expand=True)
df_b = df_b[["StudentId", "CourseId", "Grade"]]


# In[18]:


df_joined = pd.merge(df_a, df_b, on="StudentId", how="inner")


# In[19]:


df_joined = df_joined[df_joined["DOB"] >= "1995-01-01"]


# In[21]:


df_joined = df_joined[["StudentId", "Name", "CourseId", "Grade"]]


# In[22]:


print(df_joined)
df_joined.to_csv("C:/Users/Ritu/Downloads/reducer_output.csv", index=False)


# In[ ]:




