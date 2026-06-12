import pandas as pd
df=pd.read_csv("vehicles_70x70.csv")
print(df.columns)
print(df.info())
print(df.describe())

print(df.head())