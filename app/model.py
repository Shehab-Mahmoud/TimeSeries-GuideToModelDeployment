import joblib


def predict(date):
    model = joblib.load('alex_model.pkl')
    res = model.predict(date)[0]
    
    return res