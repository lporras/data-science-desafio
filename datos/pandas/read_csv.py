import pandas as pd

df = pd.read_csv("nations.csv")

print(df.shape)

print(df.head())

print(df.head(2))

df = df.drop(columns="Unnamed: 0")

print(df)