#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis
# # This the Analysis for India Premier league

# In[87]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl as xl


# # we begin by importing data, both match and deliveries data set

# In[88]:


df1= pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\python practise files\Indian Premier League\matches.csv")
df2=pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\python practise files\Indian Premier League\deliveries.csv")


# In[89]:


df1.shape


# In[90]:


df2.shape


# # we can merge both datasets into one dataset with id as acommon value

# In[91]:


df=pd.merge(df1,df2, on='id')


# In[92]:


df.head()


# # we get to understand our data

# In[93]:


df.shape


# In[94]:


df.dtypes


# # we convert date from object to datetype

# In[95]:


df.insert(4,'Date',pd.to_datetime(df.date))


# In[96]:


df.drop(columns='date',inplace=True)


# In[97]:


pd.options.display.max_columns = None


# In[98]:


df.head()


# # (1) As a sport analyst find out the most successful teams,players.

# # lets find the team which has won the league most

# In[99]:


B=df1.winner.value_counts()
B


# # showing on the graph 

# In[100]:


sns.barplot(y=B.index,x=B,orient='h')


# From our analysis acompany should endorse Mumbai Indians for its products since its the best team

# # lets find the best team per season

# In[101]:


group=df1.groupby('season')
team = group['winner'].apply(lambda x: x.value_counts().idxmax())
print(team)


# # lets see the team which won by maximum runs

# In[102]:


df1.iloc[df1['win_by_runs'].idxmax()]['winner']


# Mumbai is the team with the best batsman

# # Lets see the team which won by maximum wickets

# In[103]:


df1.iloc[df1['win_by_wickets'].idxmax()]['winner']


# # lets see the team which won by mimimum wickets

# In[104]:


df1.iloc[df1[df1['win_by_wickets'].ge(1)].win_by_wickets.idxmin()]['winner']


# # lets see the team which won by minimum runs

# In[105]:


df1.iloc[df1[df1['win_by_runs'].ge(1)].win_by_runs.idxmin()]['winner']


# From our analysis Mumbai Indians won through maximum runs and minimum runs,Kolkata Knight Riders won through maximum wickets and through mimimum wickets

# # lets find the total number of seasons played

# In[130]:


print(len(df.groupby('season')))


# # which season had the most matches

# In[107]:


plt.figure(figsize=(20,9))
sns.countplot(x='season', data=df1,order=df.season.value_counts().index)


# # Lets find the best 10 players of the match of all times.

# In[108]:


Best=df1['player_of_match'].value_counts().head(10)


# In[109]:


plt.figure(figsize=(20,9))
sns.barplot(x=Best.index,y=Best,data=df1)


# CH Gayle should be considered for endorsement by company wanting to promote there products since he is the best.

# # lets find the best players per season

# In[110]:


grouped=df1.groupby('season')
best = grouped['player_of_match'].apply(lambda x: x.value_counts().idxmax())
print(best)


# # (2) Find the factors contributing to a win or loss of a team

# # The Total number of wins each time has won against each other by 'win_by_runs'

# In[111]:


df.pivot_table(index='batting_team',columns='bowling_team',values='win_by_runs' , aggfunc='sum')


# # The Total number of wins each time has won against each other by win_by_wickets

# In[112]:


df.pivot_table(index='batting_team',columns='bowling_team',values= 'win_by_wickets' , aggfunc='sum')


# # Lets see the factors affecting a win or a loss

# In[113]:


A=df[['win_by_runs','win_by_wickets','inning','over','ball','is_super_over', 'wide_runs',
       'bye_runs', 'legbye_runs', 'noball_runs', 'penalty_runs',
       'batsman_runs', 'extra_runs',]]


# In[114]:


A.corr()


# From the correlation matrix we can conclude that there is no strong correlation between all those factors contributing to a team winning in
# any way.

# # The End

# # I tried to use Autoviz feature to help me visualize the data better

# In[124]:


import pandas as pd


# In[125]:


from autoviz.AutoViz_Class import AutoViz_Class


# In[126]:


AV= AutoViz_Class()


# In[127]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[128]:


df1="C:/Users/HP/OneDrive/Desktop/python practise files/Indian Premier League/matches.csv"
df2="C:/Users/HP/OneDrive/Desktop/python practise files/Indian Premier League/deliveries.csv"


# In[129]:


df = AV.AutoViz(df1
    ,
    sep=",",
    depVar="",
    dfte=None,
    header=0,
    verbose=0,
    lowess=False,
    chart_format="svg",
    max_rows_analyzed=150000,
    max_cols_analyzed=30,
)


# In[ ]:





# In[ ]:




