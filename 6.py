import numpy as np
import pandas as pd
df = pd.read_csv("~/banking.csv")
print(df.describe())
print(df['education'].unique())
print(df['y'].value_counts())
print(df.mean())
a = np.array(df['marital'].unique())
print(a)
for i in a:
    m = df.loc[df['marital'] == i, 'age'].mean()
    print(i,m)
print(df.isnull().values.any())
