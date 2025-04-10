import joblib
import numpy as np
import os

# Load model once when app starts
model_path = os.path.join(os.path.dirname(__file__), 'model.joblib')
model = joblib.load(model_path)

def categorize_student(data):
    features = np.array([[data['performance'], data['attendance'], data['engagement']]])
    prediction = model.predict(features)[0]
    return prediction
