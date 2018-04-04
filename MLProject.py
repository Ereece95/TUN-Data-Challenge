# -*- coding: utf-8 -*-
"""
@author: Aidan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
Column Names: (Internal Event Name)	
(Event ID)	(Team Division)	(Company)	
(Number of Participants)	(Total Fees Paid)
(Team Total Confirmed ($))	(Total Online Gifts($))
(Total Offline Confirmed Gifts($))
(Total Offline Unconfirmed Gifts($))	(Team Goal($))
(Total Confirmed Gifts in Team History($))
(Previous Event Fiscal Year)	(Previous Event Confirmed Gifts($))
(Previous Event Team Members)	(Fiscal Year) 
'''

csvFile = "CleanedData.csv"

df = pd.read_csv(csvFile)
df = df.fillna(value='')

ptAmountRaised = pd.pivot_table(df[df['Fiscal Year'] != 2018], values='Team Total Confirmed ($)', index=['Previous Event Fiscal Year'], columns=['Fiscal Year'], aggfunc=np.sum)
ptAmountRaised = ptAmountRaised.round(2);

ptAvgNumParticipants = pd.pivot_table(df[df['Fiscal Year'] != 2018], values='Number of Participants', index=['Previous Event Fiscal Year'], columns=['Fiscal Year'], aggfunc=np.average)
ptAvgNumParticipants = ptAvgNumParticipants.round();

print(ptAmountRaised.to_string(na_rep=''))
plotAmountRaised = ptAmountRaised.T.plot.bar(title='Amount Raised by Year (New vs. Existing Corporate Teams)')


print(ptAvgNumParticipants.to_string(na_rep=''))
plotAmountRaised = ptAvgNumParticipants.T.plot.bar(title='Average Number of Participants by Year(New vs. Existing Corporate Teams)')




