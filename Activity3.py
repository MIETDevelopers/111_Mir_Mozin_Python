#!/usr/bin/env python
# coding: utf-8

# In[31]:


# a) Count the number of alphabets in the given string

a = "Welcome to Python world"
count = 0
for i in a:
    if (i.isalpha()):
        count = count+1
print("Number of alphabets:",count)


# In[32]:


# b) To extract characters in the given range from given string

startrange = int(input("Enter starting range: "))
endrange = int(input("Enter ending range: "))
print(a[startrange:endrange])


# In[33]:


# c) Check if the string is alphanumeric or not

a = "Welcome to Python world"
print(a.isalnum())


# In[ ]:




