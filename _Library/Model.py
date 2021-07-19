import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def Model_Predict(X_train, y_train):
    model = RandomForestRegressor(n_estimators = 200,
                                #max_depth = 10,
                                #max_features = 5,
                                random_state = 0,
                                )
    model.fit(X_train, y_train)
    return model

def Prediction(model, X_test, y_test):
    y_pred = model.predict(X_test).round()
    y_pred = pd.DataFrame(y_pred, columns=["Predicted price"])
    y_test = pd.DataFrame(y_test, columns=["Pris:A(kr):O"])

    y_test.reset_index(drop=True, inplace=True)
    y_pred.reset_index(drop=True, inplace=True)
    y_concat = pd.concat([y_test, y_pred], axis=1)
    y_concat['Percentage diff'] = ((y_concat['Predicted price'] - y_concat['Pris:A(kr):O']) / y_concat['Predicted price']*100).round()

    sns.jointplot(x="Pris:A(kr):O", y="Predicted price", data=y_concat, height=10, kind="reg", joint_kws={'line_kws': {'color': 'red'}})

    yt, yp = y_concat['Pris:A(kr):O'], y_concat['Predicted price']
    print(f"MSE: {mean_squared_error(yt, yp)} \nMAE: {mean_absolute_error(yt, yp)} \nMAPE: {np.mean(np.abs((np.array(yt) - np.array(yp)) / np.array(yt))) * 100} \nR2: {r2_score(yt, yp)}")
    return y_concat