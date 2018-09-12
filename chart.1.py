import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("margins/margins_2018_09_12.csv")
print(df.describe())

left = np.array([1, 2, 3, 4, 5, 6])
height = np.array([100, 300, 200, 500, 400])
#x = range(len(df[]))
plt.plot(left, height)
plt.show()
plt.clf()