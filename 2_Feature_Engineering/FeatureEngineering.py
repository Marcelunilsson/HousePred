#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns

import sys; sys.path.insert(0, '..')
from _Library import Data_PreProcessing as pre

from timeit import default_timer as ti
#%%
#from IPython.core.display import display, HTML
#display(HTML("<style>.container { width:100% !important; }</style>"))

# Read The formated dataframe
df = pd.read_feather("../1_CleanData/CleanedData.feather").set_index("id")

#Mean from two categories
def mean2(df, cat1, cat2, meanCat):
    nestedDict = {c1:{c2:df[(df[cat1] == c1) & (df[cat2]==c2)][meanCat].mean() 
                      for c2 in df[df[cat1] == c1][cat2].unique()} 
                  for c1 in df[cat1].unique()}
    return df[[cat1, cat2, meanCat]].apply(lambda row: nestedDict[row[cat1]][row[cat2]], axis = 1) 


#Mean from tree categories
def mean3(df, cat1, cat2, cat3, meanCat):
    nestedDict = {c1:{c2:{c3:df[(df[cat1] == c1) & (df[cat2]==c2) & (df[cat3] == c3)][meanCat].mean() 
                          for c3 in df[(df[cat1] == c1) & (df[cat2]==c2)][cat3].unique()}
                      for c2 in df[df[cat1] == c1][cat2].unique()}
                  for c1 in df[cat1].unique()}
    return df[[cat1, cat2, cat3, meanCat]].apply(lambda row: nestedDict[row[cat1]][row[cat2]][row[cat3]], axis = 1) 


#Mean from four categories
def mean4(df, cat1, cat2, cat3, cat4, meanCat):
    nestedDict = {c1:{c2:{c3:{c4:df[(df[cat1] == c1) & (df[cat2]==c2) & (df[cat3] == c3) & (df[cat4]==c4)][meanCat].mean() 
                              for c4 in df[(df[cat1] == c1) & (df[cat2]==c2) & (df[cat3]==c3)][cat4].unique()}
                          for c3 in df[(df[cat1] == c1) & (df[cat2]==c2)][cat3].unique()}
                      for c2 in df[df[cat1] == c1][cat2].unique()}
                  for c1 in df[cat1].unique()}
    return df[[cat1, cat2, cat3, cat4, meanCat]].apply(lambda row: nestedDict[row[cat1]][row[cat2]][row[cat3]][row[cat4]], axis = 1)

#%%
df = pre.Creating_New_Features(df)
#%%
df = pd.read_feather("EngineeredData.feather").set_index("id")
# Mean value of 'KvmPris:A(kr):O' in the 'Stadsdel:S:Sd' per 'Rum:A(st):O'
t1 = ti()
df["MedelKvmPrisRum:A(kr):Sd"] = mean2(df, 'Stadsdel:S:Sd', 'Rum:A(st):O', 'KvmPris:A(kr):O')
t2 = ti()
print(t2-t1)
df.reset_index().to_feather("EngineeredData.feather")
#%%
df = pd.read_feather("EngineeredData.feather").set_index("id")
# Mean value of 'KvmPris:A(kr):O' in the 'Stad:S:S' per 'Rum:A(st):O'
t1 = ti()
df["MedelKvmPrisRum:A(kr):S"] = mean2(df, 'Stad:S:S', 'Rum:A(st):O', 'KvmPris:A(kr):O')
t2 = ti()
print(t2-t1)
df.reset_index().to_feather("EngineeredData.feather")


df = pd.read_feather("EngineeredData.feather").set_index("id")
# Mean value of 'KvmPris:A(kr):O' in the 'Kommun:S:K' per 'Rum:A(st):O'
t1 = ti()
df["MedelKvmPrisRum:A(kr):K"] = mean2(df, 'Kommun:S:K', 'Rum:A(st):O', 'KvmPris:A(kr):O')
t2 = ti()
print(t2-t1)
df.reset_index().to_feather("EngineeredData.feather")


df = pd.read_feather("EngineeredData.feather").set_index("id")
# Mean value of 'Pris:A(kr):O' in the 'Stadsdel:S:Sd' per 'Rum:A(st):O'
t1 = ti()
df["MedelPrisRum:A(kr):Sd"] = mean2(df, 'Stadsdel:S:Sd', 'Rum:A(st):O', 'Pris:A(kr):O')
t2 = ti()
print(t2-t1)
df.reset_index().to_feather("EngineeredData.feather")

df = pd.read_feather("EngineeredData.feather").set_index("id")
# Mean value of 'Pris:A(kr):O' in the 'Stad:S:S' per 'Rum:A(st):O'
t1 = ti()
df["MedelPrisRum:A(kr):S"] = mean2(df, 'Stad:S:S', 'Rum:A(st):O', 'Pris:A(kr):O')
t2 = ti()
print(t2-t1)
df.reset_index().to_feather("EngineeredData.feather")

df = pd.read_feather("EngineeredData.feather").set_index("id")
# Mean value of 'Pris:A(kr):O' in the 'Kommun:S:K' per 'Rum:A(st):O'
t1 = ti()
df["MedelPrisRum:A(kr):K"] = mean2(df, 'Kommun:S:K', 'Rum:A(st):O', 'Pris:A(kr):O')
t2 = ti()
print(t2-t1)
df.reset_index().to_feather("EngineeredData.feather")


df = pd.read_feather("EngineeredData.feather").set_index("id")
# Mean value of 'KvmPris:A(kr):O' in the 'Stadsdel:S:Sd' per 'Rum:A(st):O' and per 'År:N:Å'
t1 = ti()
df["MedelKvmPrisRum:A(kr):SdÅ"] = mean3(df, 'Stadsdel:S:Sd', 'Rum:A(st):O', 'År:N:Å',  'KvmPris:A(kr):O')
t2 = ti()
print(t2-t1)
df.reset_index().to_feather("EngineeredData.feather")


df = pd.read_feather("EngineeredData.feather").set_index("id")
# Mean value of 'KvmPris:A(kr):O' in the 'Stad:S:S' per 'Rum:A(st):O' and per 'År:N:Å'
t1 = ti()
df["MedelKvmPrisRum:A(kr):SÅ"] = mean3(df, 'Stad:S:S', 'Rum:A(st):O', 'År:N:Å', 'KvmPris:A(kr):O')
t2 = ti()
print(t2-t1)
df.reset_index().to_feather("EngineeredData.feather")


df = pd.read_feather("EngineeredData.feather").set_index("id")
# Mean value of 'KvmPris:A(kr):O' in the 'Kommun:S:K' per 'Rum:A(st):O' and per 'År:N:Å'
t1 = ti()
df["MedelKvmPrisRum:A(kr):KÅ"] = mean3(df, 'Kommun:S:K', 'Rum:A(st):O', 'År:N:Å', 'KvmPris:A(kr):O')
t2 = ti()
print(t2-t1)
df.reset_index().to_feather("EngineeredData.feather")

df = pd.read_feather("EngineeredData.feather").set_index("id")
# Mean value of 'Pris:A(kr):O' in the 'Stadsdel:S:Sd' per 'Rum:A(st):O' and per 'År:N:Å'
t1 = ti()
df["MedelPrisRum:A(kr):SdÅ"] = mean3(df, 'Stadsdel:S:Sd', 'Rum:A(st):O', 'År:N:Å', 'Pris:A(kr):O')
t2 = ti()
print(t2-t1)
df.reset_index().to_feather("EngineeredData.feather")


df = pd.read_feather("EngineeredData.feather").set_index("id")
# Mean value of 'Pris:A(kr):O' in the 'Stad:S:S' per 'Rum:A(st):O' and per 'År:N:Å'
t1 = ti()
df["MedelPrisRum:A(kr):SÅ"] = mean3(df, 'Stad:S:S', 'Rum:A(st):O', 'År:N:Å', 'Pris:A(kr):O')
t2 = ti()
print(t2-t1)
df.reset_index().to_feather("EngineeredData.feather")


df = pd.read_feather("EngineeredData.feather").set_index("id")
# Mean value of 'Pris:A(kr):O' in the 'Kommun:S:K' per 'Rum:A(st):O' and per 'År:N:Å'
t1 = ti()
df["MedelPrisRum:A(kr):KÅ"] = mean3(df, 'Kommun:S:K', 'Rum:A(st):O', 'År:N:Å', 'Pris:A(kr):O')
t2 = ti()
print(t2-t1)
df.reset_index().to_feather("EngineeredData.feather")


df = pd.read_feather("EngineeredData.feather").set_index("id")
# Mean value of 'KvmPris:A(kr):O' in the 'Lat0Deci:N:O', 'Long0Deci:N:O' per 'Rum:A(st):O'
t1 = ti()
df["MedelKvmPrisRumLatLong0Deci:A(kr):"] = mean3(df, 'Lat0Deci:N:O', 'Long0Deci:N:O', 'Rum:A(st):O', 'KvmPris:A(kr):O')
t2 = ti()
print(t2-t1)
df.reset_index().to_feather("EngineeredData.feather")


df = pd.read_feather("EngineeredData.feather").set_index("id")
# Mean value of 'KvmPris:A(kr):O' in the 'Lat1Deci:N:O', 'Long1Deci:N:O' per 'Rum:A(st):O'
t1 = ti()
df["MedelKvmPrisRumLatLong1Deci:A(kr):"] = mean3(df, 'Lat1Deci:N:O', 'Long1Deci:N:O', 'Rum:A(st):O', 'KvmPris:A(kr):O')
t2 = ti()
print(t2-t1)
df.reset_index().to_feather("EngineeredData.feather")


df = pd.read_feather("EngineeredData.feather").set_index("id")
# Mean value of 'KvmPris:A(kr):O' in the 'Lat2Deci:N:O', 'Long2Deci:N:O' per 'Rum:A(st):O'
t1 = ti()
df["MedelKvmPrisRumLatLong2Deci:A(kr):"] = mean3(df, 'Lat2Deci:N:O', 'Long2Deci:N:O', 'Rum:A(st):O', 'KvmPris:A(kr):O')
t2 = ti()
print(t2-t1)
df.reset_index().to_feather("EngineeredData.feather")


df = pd.read_feather("EngineeredData.feather").set_index("id")
# Mean value of 'KvmPris:A(kr):O' in the 'Lat3Deci:N:O', 'Long3Deci:N:O' per 'Rum:A(st):O'
t1 = ti()
df["MedelKvmPrisRumLatLong3Deci:A(kr):"] = mean3(df, 'Lat3Deci:N:O', 'Long3Deci:N:O', 'Rum:A(st):O', 'KvmPris:A(kr):O')
t2 = ti()
print(t2-t1)
df.reset_index().to_feather("EngineeredData.feather")

df = pd.read_feather("EngineeredData.feather").set_index("id")
# Mean value of 'KvmPris:A(kr):O' in the 'Lat0Deci:N:O', 'Long0Deci:N:O' per 'Rum:A(st):O' and per 'År:N:Å'
t1 = ti()
df["MedelKvmPrisRumLatLong0Deci:A(kr):Å"] = mean4(df, 'Lat0Deci:N:O', 'Long0Deci:N:O', 'Rum:A(st):O', 'År:N:Å', 'KvmPris:A(kr):O')
t2 = ti()
print(t2-t1)
df.reset_index().to_feather("EngineeredData.feather")

df = pd.read_feather("EngineeredData.feather").set_index("id")
# Mean value of 'KvmPris:A(kr):O' in the 'Lat1Deci:N:O', 'Long1Deci:N:O' per 'Rum:A(st):O' and per 'År:N:Å'
t1 = ti()
df["MedelKvmPrisRumLatLong1Deci:A(kr):Å"] = mean4(df, 'Lat1Deci:N:O', 'Long1Deci:N:O', 'Rum:A(st):O', 'År:N:Å', 'KvmPris:A(kr):O')
t2 = ti()
print(t2-t1)
df.reset_index().to_feather("EngineeredData.feather")

df = pd.read_feather("EngineeredData.feather").set_index("id")
# Mean value of 'KvmPris:A(kr):O' in the 'Lat2Deci:N:O', 'Long2Deci:N:O' per 'Rum:A(st):O' and per 'År:N:Å'
t1 = ti()
df["MedelKvmPrisRumLatLong2Deci:A(kr):Å"] = mean4(df, 'Lat2Deci:N:O', 'Long2Deci:N:O', 'Rum:A(st):O','År:N:Å', 'KvmPris:A(kr):O')
t2 = ti()
print(t2-t1)
df.reset_index().to_feather("EngineeredData.feather")


df = pd.read_feather("EngineeredData.feather").set_index("id")
# Mean value of 'KvmPris:A(kr):O' in the 'Lat3Deci:N:O', 'Long3Deci:N:O' per 'Rum:A(st):O' and per 'År:N:Å'
t1 = ti()
df["MedelKvmPrisRumLatLong3Deci:A(kr):Å"] = mean4(df, 'Lat3Deci:N:O', 'Long3Deci:N:O', 'Rum:A(st):O','År:N:Å', 'KvmPris:A(kr):O')
t2 = ti()
print(t2-t1)
df.reset_index().to_feather("EngineeredData.feather")


df = pd.read_feather("EngineeredData.feather").set_index("id")

df.reset_index().to_feather("EngineeredData.feather")


df = pd.read_feather("EngineeredData.feather").set_index("id")

df.reset_index().to_feather("EngineeredData.feather")

