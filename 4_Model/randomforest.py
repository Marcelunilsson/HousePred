#%%
import sys; sys.path.insert(0, '..')
from _Library import _Library as lib
import pandas as pd

# %%

X = pd.read_feather("../3_Feature Selection/X.feather").set_index("id")
y = pd.read_feather("../3_Feature Selection/y.feather").set_index("id")
model, y_concat = lib.mod.random_forest(X, y)
# %%


