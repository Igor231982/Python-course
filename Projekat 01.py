#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt 
#importing library
df = pd.read_csv("C:\\Users\\Igor\\Desktop\\cbb19.csv")
#path to file


# In[3]:



df2 = df.sort_values(by='W', ascending=0) 
#sorting values in ascending order
df3 = df2[:5]
#indexing five teams
df3.plot(x = 'TEAM',y = 'W', kind = 'bar', label = 'Wins')
plt.savefig('plot1.png')
plt.show()


# In[4]:


df4 = df.sort_values(by='W', ascending=1)
#sorting values in descending order
df5 = df4[:5]
#indexing five teams
df5.plot(x = 'TEAM',y = 'W', kind = 'bar', label = 'Wins')
plt.savefig('plot2.png')
plt.show()


# In[5]:


df6 = df.sort_values(by='G', ascending=1)
#sorting values in descending order
df7 = df6[:5]
#indexing five teams
df7.plot(x = 'TEAM',y = 'G', kind = 'bar', label = 'Games')
plt.savefig('plot3.png')
plt.show()


# In[6]:


plt.show()


# In[8]:


x = df3["W"]
y = df3["G"]
l = df3["TEAM"]

label = l
won_games = x
played_games = y

x =np.arange(len(label))
#label location, return evenly spaced values within a given interval.
width=0.35
#width oof bars


fig, ax = plt.subplots(figsize=(15,8))
#Create a figure and a set of subplots.
rects1 = ax.bar(x - width/2, won_games, width, label='Wons')
#react of the most wons
rects2 = ax.bar(x + width/2, played_games, width, label='Games')
#react for the most games played

ax.set_ylabel('Scores')
#name of the y label
ax.set_title('Scores by wons')
#title for the bar chart
ax.set_xticks(x)
ax.set_xticklabels(label)
ax.legend()
#function for bar chart
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0,3),
            textcoords='offset points',
            ha='center',va='bottom')


    
autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
plt.savefig('plot4.png')
plt.show()


# In[ ]:




