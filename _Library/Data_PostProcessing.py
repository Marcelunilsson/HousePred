import joblib
import pickle


def Export_Variables(model, Scaler_Fitted, encoder, model_name):
    pickle.dump(model, open(f'../_Library/Variables/model_{model_name}.sav', 'wb'))
    joblib.dump(Scaler_Fitted, f'../_Library/Variables/scaler_{model_name}.joblib')
    joblib.dump(encoder, f'../_Library/Variables/encoder_{model_name}.joblib')
