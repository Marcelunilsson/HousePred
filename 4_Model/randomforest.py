<<<<<<< HEAD
=======
#%%
>>>>>>> 2fee0243e3147665a6c579b7cb1b59ff7bebd945
import sys; sys.path.insert(0, '..')
from _Library import _Library as lib
import pandas as pd

<<<<<<< HEAD


X = pd.read_feather("../3_Feature_Selection/X.feather").set_index("id")
y = pd.read_feather("../3_Feature_Selection/y.feather").set_index("id")
model, y_concat = lib.mod.random_forest(X, y)

=======
# %%

X = pd.read_feather("../3_Feature Selection/X.feather").set_index("id")
y = pd.read_feather("../3_Feature Selection/y.feather").set_index("id")
model, y_concat = lib.mod.random_forest(X, y)
# %%
>>>>>>> 2fee0243e3147665a6c579b7cb1b59ff7bebd945


