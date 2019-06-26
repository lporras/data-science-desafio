import pandas as pd

df = pd.read_csv("nations.csv")
df = df.drop(columns="Unnamed: 0")

df.loc[8, "life"]

type(df.loc[8, "life"])

df_subset = df.loc[:, ["gdp", "school", "adfert", "chldmort"]]

type(df_subset)

df_subset.head()

df_subset_2 = df.loc[:, "gdp":"pop"]

df_subset_2.head()

df_americas = df[df["region"] == "Americas"]

df_americas.head()

df_americas[df_americas["gdp"] == df_americas["gdp"].max()]

type(df_americas[df_americas["gdp"] == df_americas["gdp"].max()])

df_americas[df_americas["gdp"] == df_americas["gdp"].max()]["country"]