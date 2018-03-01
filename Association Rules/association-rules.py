import numpy as np
import pandas as pd



f =  pd.read_csv('data.csv', dtype='str', header=None)
data = np.array(f.astype(str))
items = []

for d in data:
    items = np.union1d(items, d)

items = np.delete(items, np.where(items=='nan'))
level_1 = np.ndarray(shape=(0, 2))
print(level_1.shape)

for item in items:
    idxes = np.where(data == item)[0]
    level_1 = np.append(level_1, [[item, len(idxes)]], axis=0)

print(level_1)
