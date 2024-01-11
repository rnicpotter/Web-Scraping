#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


def find_nth_pos(array,x,n):

    y = 0
    for i in range(len(array)):
        if array[i] ==x :
            y += 1
            if y == n:
                return i
    return 'no'


# In[7]:


url = 'https://myanimelist.net/topanime.php?limit=0'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[10]:


anime_list_titles = soup.find_all('tr', class_ = 'table-header')

anime_list_titles


# In[11]:


anime_list = soup.find_all('a', class_ = 'hoverinfo_trigger')


# In[8]:


anime_list = soup.find_all('a', class_ = 'hoverinfo_trigger')
anime_list_rat = soup.find_all('td', class_ = 'score')
anime_list_info = soup.find_all('div', class_ = 'information di-ib mt4')


# In[9]:


temp_list_rat = []

for q in range(52):
    if q > 1:
        rat1 = find_nth_pos(str(anime_list_rat[q-1]), '>',5)
        rat2 = find_nth_pos(str(anime_list_rat[q-1]), '<',6)
        temp_list_rat.append((str(anime_list_rat[q-1]))[rat1+1:rat2])
        
temp_list_name = []

for q in range(100):
    if q % 2 == 1:
        anime_list[q]
        idx1 = find_nth_pos(str(anime_list[q]), '>', 1)
        idx2 = find_nth_pos(str(anime_list[q]), '<', 2)
        temp_list_name.append((str(anime_list[q]))[idx1+1:idx2])
        
temp_list_ep = []

for w in range(50):
    t1 = find_nth_pos(str(anime_list_info[w]), '>', 1)
    t2 = find_nth_pos(str(anime_list_info[w]), '<', 2)
    #print(str(anime_list_info[w])[t1+1:t2])
    temp_str1 = str(anime_list_info[w])[t1+1:t2]
    temp_list_ep.append(temp_str1.strip())

temp_list_date = []

for w in range(50):
    d1 = find_nth_pos(str(anime_list_info[w]), '>', 2)
    d2 = find_nth_pos(str(anime_list_info[w]), '<', 3)
    #print(str(anime_list_info[w])[d1+1:d2])
    temp_str2 = str(anime_list_info[w])[d1+1:d2]
    temp_list_date.append(temp_str2.strip())
    
temp_list_mem = []

for w in range(50):
    m1 = find_nth_pos(str(anime_list_info[w]), '>', 3)
    m2 = find_nth_pos(str(anime_list_info[w]), '<', 4)
    #print(str(anime_list_info[w])[m1+1:m2])
    temp_str = str(anime_list_info[w])[m1+1:m2]
    temp_list_mem.append(temp_str.strip())


# In[6]:


df = pd.DataFrame({
    "A": [1, 2],
    "B": [4, 5],
    "C": [1, 2],
    "D": [4, 5],
    "E": [1, 2]
})
df = df.rename(columns={"A": "Title", "B": "Rating", "C": "Number of Episodes", "D": "Running Dates", "E": "Total Members"})
df = df.iloc[2:]

for idx in range(len(temp_list_rat)):
    length = len(df)
    ##print(temp_list_name[idx])
    ##print(temp_list_rat[idx])
    df.loc[length] = [temp_list_name[idx], temp_list_rat[idx], temp_list_ep[idx], temp_list_date[idx], temp_list_mem[idx]]

df


# In[10]:


for idx in range(len(temp_list_rat)):
    length = len(df)
    ##print(temp_list_name[idx])
    ##print(temp_list_rat[idx])
    df.loc[length] = [temp_list_name[idx], temp_list_rat[idx], temp_list_ep[idx], temp_list_date[idx], temp_list_mem[idx]]

df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




