#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy
data=numpy.loadtxt('EuO.txt')


# In[13]:


Export = open("EuOBand.txt",'w')


# In[28]:


nband = 37;       # Specify how many bands you want to plot
for i in range (0,int(len(data)/nband)):   # Calculate how many points for each band
    Export.write('%.8f'%(data[i][0]));     # First column is the k points
    for j in range(0,nband):
        Export.write('\t');
        Export.write('%.8f'%(data[int(len(data)/nband)*j+i][1])); # Next nband columns are energy of each band 
    Export.write('\r\n');


# In[29]:


Export.close


# In[ ]:




