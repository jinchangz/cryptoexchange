import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("margins/margins_2018_09_12.csv")
print(df.describe())
for ex_pair in df.columns:
    
    plt.figure(1)
    plt.hist(df[ex_pair],bins=50,align='mid',ec='black')
    plt.xticks(rotation=45)
    plt.title('histogram_' + ex_pair)
    plt.xlabel('margin')
    plt.ylabel('count')
    plt.savefig('histograms/margin_' + ex_pair + '.png')
    plt.pause(.01)

    plt.clf()