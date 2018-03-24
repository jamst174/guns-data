
# coding: utf-8

# In[1]:


import csv
file = open('guns.csv', 'r')
csvreader = csv.reader(file)


# In[2]:


data = list(csvreader)


# In[3]:


print(data[:5])


# In[4]:


headers = data[0]


# In[5]:


data = data[1:]


# In[6]:


years = [year[1] for year in data]


# In[7]:


year_counts = {}
for year in years:
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1


# In[8]:


print(year_counts)


# In[9]:


import datetime
dates = [datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in data]


# In[10]:


print(dates[:5])


# In[11]:


date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1


# In[12]:


for dc in date_counts:
    print(dc, date_counts[dc])


# In[13]:


def count_stuff(col, data):
    counter = {}
    temps = [row[col] for row in data]
    for temp in temps:
        if temp in counter:
            counter[temp] += 1
        else:
            counter[temp] = 1
    return counter


# In[14]:


sex_counts = count_stuff(5, data)


# In[15]:


print(sex_counts)


# In[16]:


race_counts= count_stuff(7, data)


# In[17]:


print(race_counts)


# majority of gun deaths are white men
# month, year has little impact

# In[18]:


file = open('census.csv', 'r')
csvreader = csv.reader(file)
census = list(csvreader)
print(census)


# In[19]:


mapping = {'Native American/Native Alaskan': 3739506, 'Asian/Pacific Islander': 15834141, 'Black': 40250635, 'Hispanic': 44618105, 'White': 197318956}


# In[20]:


race_per_hundredk = {}
for race in race_counts:
    race_per_hundredk[race] = race_counts[race]/mapping[race] * 100000


# In[21]:


print(race_per_hundredk)


# In[22]:


intents = [row[3] for row in data]


# In[24]:


races = [row[7] for row in data]


# In[26]:


homicide_race_counts = {}


# In[27]:


for i, race in enumerate(races):
    if intents[i] == 'Homicide':
        if race in homicide_race_counts:
            homicide_race_counts[race] += 1
        else:
            homicide_race_counts[race] = 1


# In[28]:


print(homicide_race_counts)


# In[29]:


for race in homicide_race_counts:
    homicide_race_counts[race] = homicide_race_counts[race]/mapping[race] * 100000


# In[30]:


print(homicide_race_counts)

