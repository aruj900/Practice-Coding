
# coding: utf-8

# In[1]:

import csv
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
final_data=[]
for elm in rows:
    split_list= elm.split(',')
    final_data.append(split_list)
print(final_data)    


# In[ ]:



