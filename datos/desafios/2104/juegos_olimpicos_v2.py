import pandas as pd
import numpy as np

df = pd.read_csv("athlete_events.csv")

gold_athletes = df[df['Medal'] == 'Gold']
silver_athletes = df[df['Medal'] == 'Silver']
bronze_athletes = df[df['Medal'] == 'Bronze']
na_athletes = df[df['Medal'].isna()]

def set_female_column(dataFrame):
  female_column = np.where(dataFrame['Sex'] == 'F', 1, 0)
  dataFrame['Female'] = female_column

set_female_column(gold_athletes)
set_female_column(silver_athletes)
set_female_column(bronze_athletes)
set_female_column(na_athletes)



