#!/usr/bin/env python
# coding: utf-8

# 1.Write a Python program which accepts a list named : randomList = ['a', 0,2] Use exception handling using try-catch which gives the output as:

# In[1]:


import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)


# In[ ]:





# In[2]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




