# mlops-credit-risk
# MLOps Credit Risk Microservice

An end-to-end MLOps pipeline for automated credit risk prediction using XGBoost, FastAPI, Docker, and GitHub Actions.

## 🏗️ Architecture
1. **Model Experimentation:** Trained an XGBoost classifier logged with **MLflow** in Google Colab.
2. **API Service:** Engineered a RESTful microservice with **FastAPI** and **Pydantic** data validation.
3. **Containerization:** Packaged using **Docker** for cross-environment reproducibility.
4. **CI/CD Pipeline:** Automated unit testing (`pytest`) and Docker container verification using **GitHub Actions**.

## 🚀 How to Run Locally

### 1. Run with Docker
```bash
docker build -t credit-risk-api .
docker run -p 8000:8000 credit-risk-api
