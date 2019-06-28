import pandas as pd

df = pd.read_csv("athlete_events.csv")

ejercicio_1 = df.shape
print(ejercicio_1)

ejercicio_2 = df['Year'].unique().shape[0]

summer = df['Season'] == 'Summer'
winter = df['Season'] == 'Winter'
summer_athletes = df[summer]
winter_athletes = df[winter]
summer_and_winter_athletes = pd.concat([summer_athletes, winter_athletes], ignore_index=True)
ejercicio_3 = summer_and_winter_athletes['Season'].value_counts("%")

first_year_summer = summer_athletes['Year'].min()
ejercicio_4 = summer_athletes[summer_athletes['Year'] == first_year_summer]['City'].unique()

first_year_winter = winter_athletes['Year'].min()
ejercicio_5 = winter_athletes[winter_athletes['Year'] == first_year_winter]['City'].unique()

ejercicio_6 = df['NOC'].value_counts().head(10)

ejercicio_7 = df['Medal'].value_counts("%")

ejercicio_8 = summer_athletes[summer_athletes['Year'] == first_year_summer]['NOC'].unique()