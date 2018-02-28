import numpy as np
import pandas as pd



f =  pd.read_csv('data.csv', dtype='str', header=None)
data = np.array(f.astype(str))
items = []

for d in data:
    items = np.union1d(items, d)

items = np.delete(items, np.where(items=='nan'))
print(items.shape)
