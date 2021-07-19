import joblib
import pickle

def Export_Variables(model, Scaler_Fitted, encoder):
    pickle.dump(model, open('../_Library/Variables/model.sav', 'wb'))
    joblib.dump(Scaler_Fitted, '../_Library/Variables/scaler.joblib')
    joblib.dump(encoder, '../_Library/Variables/encoder.joblib')
