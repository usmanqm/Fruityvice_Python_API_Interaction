#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install requests


# In[4]:


import requests

response = requests.get("https://www.fruityvice.com/api/fruit/banana")


# In[16]:


url = "https://www.fruityvice.com/api/fruit/fat?min=5"


# In[17]:


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


# In[13]:


## display fruits and nutritional value in a formated table

headers = ["Fruit", "Calories", "Sugar", "Carbohydrates", "Protein", "Fat"]

print(f"{headers[0]:<15}{headers[1]:<10}{headers[2]:<10}{headers[3]:<15}{headers[4]:<10}{headers[5]:<10}")
print("=" * 70)

for fruit in data:
    name = fruit.get("name", "N/A")
    nutrition = fruit.get("nutritions", {})

    calories = nutrition.get("calories", 0)
    sugar = nutrition.get("sugar", 0)
    carbohydrates = nutrition.get("carbohydrates", 0)
    protein = nutrition.get("protein", 0)
    fat = nutrition.get("fat", 0)

    print(f"{name:<15}{calories:<10}{sugar:<10}{carbohydrates:<15}{protein:<10}{fat:<10}")


# In[20]:


import matplotlib.pyplot as plt

## plotting nutritional information

# Step 2: Extract values
names = []
sugar = []
protein = []
fat = []
calories = []

for fruit in data:
    names.append(fruit["name"])
    nutrients = fruit["nutritions"]

    sugar.append(nutrients["sugar"])
    protein.append(nutrients["protein"])
    fat.append(nutrients["fat"])
    calories.append(nutrients["calories"])

# Step 3: Plot (bar chart example)
x = range(len(names))

plt.figure(figsize=(10, 5))

plt.bar(x, sugar, label="Sugar")
plt.bar(x, protein, label="Protein", bottom=sugar)
plt.bar(x, fat, label="Fat", bottom=[s + p for s, p in zip(sugar, protein)])

plt.xticks(x, names, ha="center")
plt.ylabel("Grams per 100g")
plt.title("Nutritional Profile (Fat ≥ 5)")
plt.legend()

plt.tight_layout()
plt.show()


# In[ ]:




