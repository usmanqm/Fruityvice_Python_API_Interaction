#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install requests


# In[4]:


import requests

response = requests.get("https://www.fruityvice.com/api/fruit/banana")


# In[5]:


url = "https://www.fruityvice.com/api/fruit/fat?min=5"


# In[6]:


response = requests.get(
    "https://www.fruityvice.com/api/fruit/fat",
    params={"min": 5},
)

print(response.url)     # confirm that requests built the right URL


# In[10]:


print(response.status_code)     # hopefully, 200

data = response.json()          # parses the JSON response into a Python object
print(data)                     # inspect the output


# In[11]:


## Look up your least favourite fruit by name and print its protein content.

least_favourite = "Avocado"

for fruit in data:
    if fruit["name"] == least_favourite:
        print("Least favourite fruit:", fruit["name"])
        print("Protein:", fruit["nutritions"]["protein"], "g")
        break


# In[12]:


## Request all fruits and find the one with the highest sugar content

highest_sugar = max(data, key=lambda fruit: fruit["nutritions"]["sugar"])

print("Fruit with the highest sugar content:")
print("Name:", highest_sugar["name"])
print("Sugar:", highest_sugar["nutritions"]["sugar"], "g")


# In[ ]:




