# Other imports ---------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Random forest imports ---------------------------------------------
from sklearn.ensemble import RandomForestRegressor


# Sklearn imports ---------------------------------------------
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split as ts

# Our Librarys -------------------------------------------------
import sys; sys.path.insert(0, '..')
from _Library import Data_PreProcessing as pre
from _Library import Data_PostProcessing as post
from _Library import Selection as sel


def train_test_split(X, y):
    """[summary]

    Args:
        X (DataFrame): Input variables
        y (DataFrame): Output variables

    Returns:
        [type]: returns X_train, X_test, y_train, y_test
    """
    return ts(X,y, test_size=0.2,random_state=101)

def predict(model, 
            X_test, y_test,
            x_axis = "y", y_axis= "y_pred"):
    y_pred = pd.DataFrame(model.predict(X_test).round(),columns=[y_axis])
    y_pred.reset_index(drop=True, inplace=True)
    y_test = pd.DataFrame(y_test, columns=[x_axis])
    y_test.reset_index(drop=True, inplace=True)
    y_concat = pd.concat([y_test, y_pred], axis=1)
    y_concat['Percentage diff'] = ((y_concat[y_axis] - y_concat[x_axis]) / y_concat[y_axis]*100).round()
    sns.jointplot(x=x_axis,
                  y=y_axis,
                  data=y_concat,
                  height=10,
                  kind="reg",
                  joint_kws={'line_kws': {'color': 'red'}})
    yt, yp = y_concat[x_axis], y_concat[y_axis]
    mse, mae, mape, r2 = (mean_squared_error(yt, yp),
                          mean_absolute_error(yt, yp),
                          np.mean(np.abs((np.array(yt) - np.array(yp))/ np.array(yt))) * 100,
                          r2_score(yt, yp))
    plt.show()
    print(f"MSE: {mse} \nMAE: {mae} \nMAPE: {mape} \nR2: {r2}")
    return y_concat
    


def random_forest(X, y, 
                  n_estimators = 200,
                  max_depth = 10,
                  max_features = 5,
                  random_state = 0
                  ):
    X = pre.Convert_to_Float32_and_String(X)
    y = pre.Convert_to_Float32_and_String(y)
    X, encoder = pre.Encoding_Data_and_Create_Encoder(X)
    y = np.ravel(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    X_train, X_test, Scaler_Fitted = pre.Create_Scaler(X_train, X_test)
    model = RandomForestRegressor(n_estimators=n_estimators,
                                  random_state = random_state)
    model.fit(X_train, y_train)
    post.Export_Variables(model, Scaler_Fitted, encoder)
    return model, predict(model, X_test, y_test)
    