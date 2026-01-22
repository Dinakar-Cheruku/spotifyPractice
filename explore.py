import numpy as np
import pandas as pd

df = pd.read_csv('data/dataset.csv')
dim_genre = pd.read_csv('data/dim_genre.csv')
fact_genre = pd.read_csv('data/fact_genre.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


print(df.describe())