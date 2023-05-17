#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("Hallo world")


# In[1]:


print ("This is my second notebook")


# In[ ]:



from project_lib import Project
project = Project.access()
storage_credentials = project.get_storage_metadata()


# In[1]:


from ibm_watson_studio_lib import access_project_or_space
wslib = access_project_or_space()

import pandas as pd

df_data_1 = pd.read_csv(wslib.mount.get_data_path('UNdata_agri_value_added_gdp.csv'))
df_data_1.head()


# In[ ]:




