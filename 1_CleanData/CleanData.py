import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import tensorflow as tf
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.express as px

import cufflinks as cf
from timeit import default_timer as ti


#Load Data set
df = pd.read_feather('_Datasets/dataset.feather').set_index("id")


# Removing NaN and Unknown values
df['rooms'] = df['rooms'].fillna(0)
df['rooms'] = df['rooms'].str.replace('Unknown','NaN', regex=True)
df['rooms'] = df['rooms'].astype(np.float32)
df['rooms'] = df['rooms'].fillna(int(df['rooms'].mean()))


# Also removing strange values
df = df[(df['rooms'].apply(lambda x: len(str(x))) < 4) & (df['rooms'] < 20)]


# sum up all the unknowns in the dataset, if there are any a list will be printed to see where
df = df[df != "Unknown"]
df = df.dropna()
print(sum(df.isnull().sum()))

#Create new formatted data frame
df2 = pd.DataFrame()
df2["Objekttyp:S:O"] = df["object_type"]
df2["Gata:S:G"] = df["address_name"]
df2["Stadsdel:S:Sd"] = df["city_part"]
df2["Stad:S:S"] = df["city"]
df2["Kommun:S:K"] = df["municipality"]
df2["Landskap:S:Ls"] = df["county"]
df2["Rum:A(st):O"] = df["rooms"].astype(np.float32)
df2["Kvm:A(st):O"] = df["square_metres"].astype(np.float32)
df2["Pris:A(kr):O"] = df["price"].astype(np.float32)
df2["KvmPris:A(kr):O"] = df["price_per_metre"].astype(np.float32)
df2["Månad:N:M"] = df["month"].astype(np.float32)
df2["År:N:Å"] = df["year"].astype(np.float32)
df2["Lat:N:O"] = df["latitude"].astype(np.float32)
df2["Long:N:O"] = df["longitude"].astype(np.float32)
df2["Arbetslöshet:P:L"] = df["unemployment_swe"].astype(np.float32)
df2["SkattTotal:P:KÅ"] = df["skatt_total_kommun"].astype(np.float32)
df2["SkattRegering:P:KÅ"] = df["skatt_till_reg"].astype(np.float32)
df2["SkattKommun:P:KÅ"] = df["skatt_till_kommun"].astype(np.float32)
df2["Snittslön:A(kr/m):LÅ"] = df["average_salary_swe"].astype(np.float32)
df2["SnittslönMän:A(tkr/å):KÅ"] = df["average_salary_county_men"].astype(np.float32)
df2["SnittslönKvinnor:A(tkr/å):KÅ"] = df["average_salary_county_women"].astype(np.float32)
df2["Snittslön:A(tkr/å):KÅ"] = df["average_salary_county"].astype(np.float32)
df2["UtbFörGym<9År:A(st):KÅ"] = df["utbildning_förgymnasial_kortare_än_9_år"].astype(np.float32)
df2["UtbFörGym9År:A(st):KÅ"] = df["utbildning_förgymnasial_9_år"].astype(np.float32)
df2["UtbGym<=2År"] = df["utbildning_gymnasial_högst_2_år"].astype(np.float32)
df2["UtbGym3År:A(st):KÅ"] = df["utbildning_gymnasial_3_år"].astype(np.float32)
df2["UtbEfterGym<3År:A(st):KÅ"] = df["utbildning_eftergymnasial_mindre_än_3_år"].astype(np.float32)
df2["UtbEfterGym>=3År:A(st):KÅ"] = df["utbildning_eftergymnasial_3_år_eller_mer"].astype(np.float32)
df2["UtbForskare:A(st):KÅ"] = df["utbildning_forskare"].astype(np.float32)
df2["UtbUppgSaknas:A(st):KÅ"] = df["utbildning_uppgift_om_nivå_saknas"].astype(np.float32)
df2["Inflyttning:A(st):KÅ"] = df["inflyttningar"].astype(np.float32)
df2["Utflyttning:A(st):KÅ"] = df["utflyttningar"].astype(np.float32)
df2["Invandring:A(st):KÅ"] = df["invandringar"].astype(np.float32)
df2["Utvandring:A(st):KÅ"] = df["utflyttningar"].astype(np.float32)
df2["FlyttningÖverskott:A(st):KÅ"] = df["flyttningsöverskott"].astype(np.float32)
df2["InvandringÖverskott:A(st):KÅ"] = df["invandringsöverskott"].astype(np.float32)
df2["InvandringÖverskott:A(st):KÅ"] = df["invandringsöverskott"].astype(np.float32)
df2["FöddaISverige:A(st):KÅ"] = df["född_i_sverige"].astype(np.float32)
df2["FöddaIUtland:A(st):KÅ"] = df["utrikes_född"].astype(np.float32)
df2["AntalMän:A(st):KÅ"] = df["antal_män"].astype(np.float32)
df2["AntalKvinnor:A(st):KÅ"] = df["antal_kvinnor"].astype(np.float32)
df2["InvånareKm:A(st):KÅ"] = df["invånare_per_km"].astype(np.float32)
df2["MedelålderMän:A(st):KÅ"] = df["average_age_by_gender_men"].astype(np.float32)
df2["MedelålderKvinnor:A(st):KÅ"] = df["average_age_by_gender_women"].astype(np.float32)
df2["Medelålder:A(st):KÅ"] = df["average_age_by_gender_total"].astype(np.float32)
df2["KrimMisshandel:A(st):KÅ"] = df["brå_misshandel"].astype(np.float32)
df2["KrimNarkotika:A(st):KÅ"] = df["brå_narkotika"].astype(np.float32)
df2["KrimNarkotikaÖverlåtelse:A(st):KÅ"] = df["brå_narkotika_överlåtelse"].astype(np.float32)
df2["KvmTomt:A(st):O"] = df["area_plot"].astype(np.float32)
df2["HarTomt:B:O"] = df["has_area_plot"].apply(str)
df2["GDP:A(Giga$):LÅ"] = df["gdp"].astype(np.float32)
df2["OMXIndex:N:LD"] = df["omx_index"].astype(np.float32)
df2["RepoRänta:P:LD"] = df["repo"].astype(np.float32)
df2["KPI:N:LÅ"] = df["kpi"].astype(np.float32)
df2["PenningMängdM1:A(mkr):LM"] = df["monetary_mkr_per_m1"].astype(np.float32)
df2["PenningMängdM2:A(mkr):LM"] = df["monetary_mkr_per_m2"].astype(np.float32)
df2["BiArea:A(Kvm):O"] = df["area_extra"].astype(np.float32)
df2["SkillnadUtropspris:A(kr):O"] = df["price_difference"].astype(np.float32)



# Save The formated dataframe
df2.reset_index().to_feather("1_CleanData/CleanedData.feather")