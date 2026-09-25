from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_predict_endpoint():
    payload = {
        "age": 30,
        "income": 50000.0,
        "loan_amount": 10000.0,
        "credit_score": 700
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "is_default_risk" in response.json()
