import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Credit Risk API Service")

class CustomerFeatures(BaseModel):
    age: int
    income: float
    loan_amount: float
    credit_score: int

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: CustomerFeatures):
    input_df = pd.DataFrame([data.model_dump()])
    # In production, this calls the loaded MLflow model
    return {
        "is_default_risk": 0,
        "default_probability": 0.12
    }
