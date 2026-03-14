# Stock Signal DevOps Microservice

A lightweight stock market microservice that retrieves financial data from the Alpha Vantage API and generates simple trading signals. The project demonstrates a DevOps workflow with containerization, automated testing, and Kubernetes deployment.

Tech Stack:

Python
FastAPI
Uvicorn
Docker
Kubernetes
GitHub Actions (CI/CD)
Pytest

Features
REST API for retrieving stock data
Basic buy/sell signal generation
Containerized with Docker
Automated testing with pytest
CI/CD pipeline using GitHub Actions
Deployable to Kubernetes

Installation
git clone https://github.com/wkletzka/stock-signal-devops.git
cd stock-signal-devops
pip install -r requirements.txt
uvicorn app.main:app --reload

API runs at locally on your device at:
http://127.0.0.1:8000

Docker
docker build -t stock-signal-service .
docker run -p 8000:8000 stock-signal-service

Kubernetes
kubectl apply -f k8s/
