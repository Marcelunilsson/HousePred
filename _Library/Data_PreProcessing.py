
import pandas as pd
import numpy as np
import joblib
import pickle
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler


def Import_Variables(model_name):
    encoder = joblib.load(f'../_Library/Variables/{model_name}/encoder_{model_name}.joblib')
    scaler = joblib.load(f'../_Library/Variables/{model_name}/scaler_{model_name}.joblib')
    model = pickle.load(open(f'../_Library/Variables/{model_name}/model_{model_name}.sav', 'rb'))
    return encoder, scaler, model

def Creating_New_Features(df):
    def Creating_Lat_Lon_Features(df):
        # Creating latitude and longitude values with different accuracy
        # Latitude accuracies
        df['Lat5Deci:N:O'] = df['Lat:N:O'].round(decimals=5)
        df['Lat4Deci:N:O'] = df['Lat:N:O'].round(decimals=4)
        df['Lat3Deci:N:O'] = df['Lat:N:O'].round(decimals=3)
        df['Lat2Deci:N:O'] = df['Lat:N:O'].round(decimals=2)
        df['Lat1Deci:N:O'] = df['Lat:N:O'].round(decimals=1)
        df['Lat0Deci:N:O'] = df['Lat:N:O'].round(decimals=0)

        # Longitude accuracies
        df['Long5Deci:N:O'] = df['Long:N:O'].round(decimals=5)
        df['Long4Deci:N:O'] = df['Long:N:O'].round(decimals=4)
        df['Long3Deci:N:O'] = df['Long:N:O'].round(decimals=3)
        df['Long2Deci:N:O'] = df['Long:N:O'].round(decimals=2)
        df['Long1Deci:N:O'] = df['Long:N:O'].round(decimals=1)
        df['Long0Deci:N:O'] = df['Long:N:O'].round(decimals=0)
        return df

    def Creating_Total_Citiziens_Feature(df):
        # Total citizens
        df['AntalInvånare:A(st):KÅ'] = df['AntalMän:A(st):KÅ'] + df['AntalKvinnor:A(st):KÅ']
        return df

    def Creating_Percentage_Features(df):
        # Columns representing percentage values
        columnsToProcent = np.array(['UtbFörGym<9År:A(st):KÅ', 'UtbFörGym9År:A(st):KÅ', 'UtbGym<=2År',
                                        'UtbGym3År:A(st):KÅ', 'UtbEfterGym<3År:A(st):KÅ',
                                        'UtbEfterGym>=3År:A(st):KÅ', 'UtbForskare:A(st):KÅ',
                                        'UtbUppgSaknas:A(st):KÅ', 'Inflyttning:A(st):KÅ',
                                        'Utflyttning:A(st):KÅ', 'Invandring:A(st):KÅ', 'Utvandring:A(st):KÅ',
                                        'FlyttningÖverskott:A(st):KÅ', 'InvandringÖverskott:A(st):KÅ',
                                        'FöddaISverige:A(st):KÅ', 'FöddaIUtland:A(st):KÅ', 'AntalMän:A(st):KÅ',
                                        'AntalKvinnor:A(st):KÅ', 'InvånareKm:A(st):KÅ', 'KrimMisshandel:A(st):KÅ',
                                        'KrimNarkotika:A(st):KÅ', 'KrimNarkotikaÖverlåtelse:A(st):KÅ'])

        df[np.array([col + "_procent" for col in columnsToProcent])] = df[columnsToProcent].apply(lambda x: 100 * x / df['AntalInvånare:A(st):KÅ'])
        return df

    def Creating_Counter_Feature(df):
        df['Counter'] = 1

    df = Creating_Lat_Lon_Features(df)
    df = Creating_Total_Citiziens_Feature(df)
    df = Creating_Percentage_Features(df)
    #df = Create_Counter_Feature(df) Vad är detta?
    return df

def Encoding_Data_and_Create_Encoder(X):
    X = X.reset_index(drop=True)
    numerical_feature_mask = X.dtypes != object
    # Filter out numerical columns into a list
    numerical_col_names = X.columns[numerical_feature_mask].tolist()
    X_numerical_col = X[numerical_col_names]
    # Create a categorical boolean mask
    categorical_feature_mask = X.dtypes == object
    # Filter out the categorical columns into a list
    categorical_col_names = X.columns[categorical_feature_mask].tolist()
    X_categorical_col = X[categorical_col_names]

    OHE = OneHotEncoder(handle_unknown='ignore')
    encoder = OHE.fit(X_categorical_col)

    # Encoding - Transforming
    X_categorical_col_fitted_and_transformed = pd.DataFrame(
        data=encoder.transform(X_categorical_col).toarray(),
        columns=encoder.get_feature_names(categorical_col_names), dtype=bool)
    # transfer true and false to 1 and 0
    X_categorical_col = X_categorical_col_fitted_and_transformed * 1
    # concatenate data
    X = pd.concat((X_numerical_col, X_categorical_col), axis=1)
    return X, encoder

def Encoding_New_Data(X, encoder):
    X = X.reset_index(drop=True)
    numerical_feature_mask = X.dtypes != object
    # Filter out numerical columns into a list
    numerical_col_names = X.columns[numerical_feature_mask].tolist()
    X_numerical_col = X[numerical_col_names]
    # Create a categorical boolean mask
    categorical_feature_mask = X.dtypes == object
    # Filter out the categorical columns into a list
    categorical_col_names = X.columns[categorical_feature_mask].tolist()
    X_categorical_col = X[categorical_col_names]
    # Encoding - Transforming
    X_categorical_col_fitted_and_transformed = pd.DataFrame(
        data=encoder.transform(X_categorical_col).toarray(),
        columns=encoder.get_feature_names(categorical_col_names), dtype=bool)
    # transfer true and false to 1 and 0
    X_categorical_col = X_categorical_col_fitted_and_transformed * 1
    # concatenate data
    X = pd.concat((X_numerical_col, X_categorical_col), axis=1)
    return X

def Convert_to_Float32_and_String(df):
    df = df.reset_index(drop=True)

    numerical_feature_mask = df.dtypes != object
    # Filter out the numerical columns into a list for easy reference later on in case you have more than a couple categorical columns
    numerical_col_names = df.columns[numerical_feature_mask].tolist()
    df_numerical_col = df[numerical_col_names]

    # Create a categorical boolean mask
    categorical_feature_mask = df.dtypes == object
    # Filter out the categorical columns into a list for easy reference later on in case you have more than a couple categorical columns
    categorical_col_names = df.columns[categorical_feature_mask].tolist()
    df_categorical_col = df[categorical_col_names]

    df_numerical_col_converted = df_numerical_col.astype(np.float32)
    df_categorical_col_converted = df_categorical_col.applymap(str)

    df = pd.concat((df_numerical_col_converted, df_categorical_col_converted), axis=1)
    return df

def Inter_Quartile_Range_Split(df):
    q1 = df['Pris:A(kr):O'].quantile(0.25)
    q3 = df['Pris:A(kr):O'].quantile(0.75)
    iqr = q3 - q1
    fence_low = q1 - 1.5 * iqr
    fence_high = q3 + 1.5 * iqr
    df = df.loc[(df['Pris:A(kr):O'] > fence_low) & (df['Pris:A(kr):O'] < fence_high)]
    return df

def Create_Scaler(X_train, X_test):
    Scaler = MinMaxScaler()
    Scaler_Fitted = Scaler.fit(X_train)
    X_train = Scaler_Fitted.transform(X_train)
    X_test = Scaler.transform(X_test)
    return X_train, X_test, Scaler_Fitted