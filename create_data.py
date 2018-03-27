import pandas as pd
from pandas import DataFrame,Series
import random

df = DataFrame(columns=['a','b','c','key'])
for i in range(10):
    df.loc[i] = [random.random()-0.5 for k in range(3)] + [chr(ord('A')+random.randint(0,25))]


df.to_csv('examples/data.csv', index=None)

