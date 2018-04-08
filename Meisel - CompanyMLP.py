# -*- coding: utf-8 -*-
"""
Spyder Editor


This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.line_width', 5000) 
pd.set_option('display.max_columns', 60) 


df = pd.read_excel('Bike_Team_Data.xlsx', header = 0,encoding='latin1')
df1 = df.dropna(subset=['Company'])
df2 = df1.sort_values(by = ['Number of Participants'])
df22 = df1.sort_values(by = ['Team Total Confirmed'])

"""BP"""
dfbpp = df2[df2['Company'].str.contains("BP") == True]    
dfbpm= df22[df22['Company'].str.contains("BP") == True]

bpgrouped = dfbpp.groupby(dfbpp['Company']).sum()
bpgrouped1 = dfbpm.groupby(dfbpm['Company']).sum()


TotalAmountPayedbp = dfbpm['Team Total Confirmed'].sum()
TotalParticipantsbp = dfbpp['Number of Participants'].sum()

"""The Houstonian Club, Hotel and Spa"""
dfhcp = df2[df2['Company'].str.contains("Houstonian Club") == True]  
dfhcm= df22[df22['Company'].str.contains("Houstonian Club") == True]

TotalAmountPayedhc = dfhcp['Team Total Confirmed'].sum()
TotalParticipantshc = dfhcm['Number of Participants'].sum()

"""Noble Drilling Services Inc."""
dfndp = df2[df2['Company'].str.contains("Noble Drilling") == True]  
dfndm= df22[df22['Company'].str.contains("Noble Drilling") == True]

TotalAmountPayednd = dfndp['Team Total Confirmed'].sum()
TotalParticipantsnd = dfndm['Number of Participants'].sum()

"""ConocoPhillips"""
dfcpp = df2[df2['Company'].str.contains("ConocoPhillips") == True]  
dfcpm= df22[df22['Company'].str.contains("ConocoPhillips") == True]

TotalAmountPayedcp = dfcpp['Team Total Confirmed'].sum()
TotalParticipantscp = dfcpm['Number of Participants'].sum()

"""Calpine Corporation"""
dfccp = df2[df2['Company'].str.contains("Calpine Corporation") == True]  
dfccm= df22[df22['Company'].str.contains("Calpine Corporation") == True]

TotalAmountPayedcc = dfccp['Team Total Confirmed'].sum()
TotalParticipantscc = dfccm['Number of Participants'].sum()

d = {'Money Raised': [TotalAmountPayedbp, TotalAmountPayedhc,TotalAmountPayednd,TotalAmountPayedcp,TotalAmountPayedcc], 
     'Participants': [TotalParticipantsbp, TotalParticipantshc,TotalParticipantsnd,TotalParticipantscp,TotalParticipantscc]}

TopEarDF = pd.DataFrame(data = d)
print(pd.DataFrame(data = d))

TopEarDF = TopEarDF.plot.scatter(x ='Money Raised', y = 'Participants' ,title='Top 5 Size of Teams Vs Amount Raised')

df = df1.plot.scatter(x ='Team Total Confirmed', y = 'Number of Participants' ,title='Size of Teams Vs Amount Raised')

print(df22)


"""
xl = pd.ExcelFile("Bike_Team_Data.xlsx")
xl.sheet_names
[u'Bike_Team_Data']
df = xl.parse("Bike_Team_Data")
df.head()
"""