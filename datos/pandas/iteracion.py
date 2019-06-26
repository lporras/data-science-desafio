import pandas as pd

df = pd.read_csv("nations.csv")
df = df.drop(columns="Unnamed: 0")

#for i in df:
#  print(i)

#for i, el in enumerate(df):
#  print(i, el)

# Recorre verticalmente de izq a derecha
for colname, serie in df.iteritems():
  print(colname)
  print(serie)
  break

for colname, serie in df.iteritems():
  tmp = pd.api.types.is_numeric_dtype(serie)
  print("{} es {}".format(colname, tmp))

for index, row_serie in df.iterrows():
  print(index)
  print(row_serie)
  print(type(row_serie))
  break
