#%%
import os
import numpy as np
import pandas as pd
import seaborn as sns
import sys; sys.path.insert(0, '..')
import matplotlib.pyplot as plt
from _Library import _Library as lib
import sys

test_name = str(sys.argv[1])

os.system("python ../3_Feature_Selection/Selection.py")
X = pd.read_feather("../3_Feature_Selection/X.feather").set_index("id")
y = pd.read_feather("../3_Feature_Selection/y.feather").set_index("id")


#%%
X = lib.pre.Convert_to_Float32_and_String(X)
y = lib.pre.Convert_to_Float32_and_String(y)
X, encoder = lib.pre.Encoding_Data_and_Create_Encoder(X)
df = X.join(y)
print(len(df.columns))
# %%
cm = df.corr()
top_cf = cm.index
plt.figure(figsize=(30, 20))

g = sns.heatmap(df[top_cf].corr(), annot=True, cmap="copper")

plt.savefig(f"{test_name}.jpg")

print(abs(df.corr()['Pris:A(kr):O']))
# #%%
# df.columns
# %%

lib.mod.random_forest(X, y, test_name)
# %%
