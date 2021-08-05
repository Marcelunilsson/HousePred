
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

import sys; sys.path.insert(0, '..')
from _Library import _Library as lib

#%pylab inline


encoder, scaler, model = lib.pre.Import_Variables()
#df = pd.read_feather('../2_Feature Engineering/EngineeredData.feather').set_index("id")
new_df = pd.read_excel('../_Datasets/new_df.xls')


new_df = lib.sel.Data_Selection(new_df)
new_df = lib.pre.Creating_New_Features(new_df)
new_df = lib.pre.Convert_to_Float32_and_String(new_df)

X, y = lib.sel.Defining_X_and_Y(new_df)
X = lib.pre.Encoding_New_Data(X, encoder)
y = np.ravel(y)
X = scaler.transform(X)



y_concat = lib.mod.predict(model=model, X_test=X, y_test=y)
print(y_concat)
