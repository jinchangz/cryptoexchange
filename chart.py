import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("margins/margins_2018_09_12.csv")
print(df.describe())
for ex_pair in df.columns:
    df[ex_pair].plot()
    plt.xticks(rotation=45)
    plt.title('chart_' + ex_pair)
    plt.xlabel('ticks')
    plt.ylabel('margin')
    plt.savefig('charts/margin_' + ex_pair + '.png')
    plt.pause(.01)
    #plt.show()
    plt.clf()