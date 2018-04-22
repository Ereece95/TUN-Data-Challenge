# Eric Reece
# Turns out I'm more brain dead than I thought
# so this is going beyond slow

# Loading in pandas and numpy
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

# CSV file to be considered
csvFile = "NationalTeamActivity.csv"

# Read in CSV as dataframe
df = pd.read_csv(csvFile)

# Find appropriate columns from CSV file
revenue_raised = df['Revenue Raised']
location = df['Location']
numteammems = df['Number of Team Member']

