from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import os

# Initialize FastAPI app
app = FastAPI(title="Fraud Detection API")

# Load model and scaler once
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")
MODEL_PATH = os.path.join(BASE_DIR, "models", "fraud_model.pkl")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Define the expected input schema
class TransactionData(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

@app.post("/predict")
def predict(data: TransactionData):
    # Convert input to numpy array and reshape
    input_data = np.array([[getattr(data, col) for col in data.__annotations__.keys()]])
    
    # Scale the input data
    input_scaled = scaler.transform(input_data)
    
    # Make prediction
    prediction = model.predict(input_scaled)
    result = "Fraudulent" if prediction[0] == 1 else "Not Fraudulent"

    return {
        "prediction": int(prediction[0]),
        "result": result
    }
