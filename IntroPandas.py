import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("E:\Users\ShivangiS\Documents\DataScience-Python3\PastHires.csv")
df.head()
print("nil")
print df.head(10)
print df.tail(5)
print df.shape
print df.size
print len(df)
print df.columns
print df["Hired"][5]
print df[["Years Experience","Hired"]]
degree_count=df["Level of Education"].value_counts()
degree_count.plot(kind='bar')
plt.show()
