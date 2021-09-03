#%%
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import pandas as pd
import os
import sys; sys.path.insert(0, '..')
from _Library import _Library as lib



os.system("python ../3_Feature_Selection/Selection.py")
X = pd.read_feather("../3_Feature_Selection/X.feather").set_index("id")
y = pd.read_feather("../3_Feature_Selection/y.feather").set_index("id")

X = lib.pre.Convert_to_Float32_and_String(X)
y = lib.pre.Convert_to_Float32_and_String(y)
X, encoder = lib.pre.Encoding_Data_and_Create_Encoder(X)
df = X.join(y)
# %%
X_new = SelectKBest(chi2, k=4).fit_transform(X, y)
# %%
