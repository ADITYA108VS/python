#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[34]:


tata_data=pd.read_csv('TTM.csv',index_col='Date',parse_dates=True)


# In[38]:


close_np=tata_data['Close'].values
close_series=tata_data[['High','Low']]


# In[ ]:


import matplotlib.pyplot as plt


# In[41]:


tata_data['Low'].plot(color='r',legend=True)
tata_data['High'].plot(color='g',legend=True)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




