import pandas as pd

df = pd.read_csv("nations.csv")
df = df.drop(columns="Unnamed: 0")

df["gdp"]

df["gdp"].isnull().sum()

df_gdp_nan = df[df["gdp"].isnull() == True]