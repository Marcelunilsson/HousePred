import joblib
import pickle
import os


def Export_Variables(model, Scaler_Fitted, encoder, model_name):
    os.mkdir(f"../_Library/Variables/{model_name}")
    pickle.dump(model, open(f'../_Library/Variables/{model_name}/model_{model_name}.sav', 'wb'))
    joblib.dump(Scaler_Fitted, f'../_Library/Variables/{model_name}/scaler_{model_name}.joblib')
    joblib.dump(encoder, f'../_Library/Variables/{model_name}/encoder_{model_name}.joblib')
