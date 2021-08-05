import pandas as pd
import numpy as np

import sys; sys.path.insert(0, '..')
from _Library import Data_PreProcessing as pre
from _Library import Selection as sel



df = pd.read_feather("../2_Feature_Engineering/EngineeredData.feather").set_index("id")

df = sel.Data_Selection(df)

df = pre.Inter_Quartile_Range_Split(df)

X, y = sel.Defining_X_and_Y(df)

y.reset_index().to_feather("y.feather")
X.reset_index().to_feather("X.feather")