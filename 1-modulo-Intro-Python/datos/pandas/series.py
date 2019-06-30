import pandas as pd

df = pd.read_csv("nations.csv")
df = df.drop(columns="Unnamed: 0")

df['region']
type(df['region'])

for i in df['region']:
  print(i)

df['region'].value_counts()

df['region'].value_counts().mean()