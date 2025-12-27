#Automated tests for the mircroservice
from fastapi.testclient import TestClient
from app.main import app #imports FastAPI app instance defined in app/main.py

client = TestClient(app) #creates fake HTTP client 

def testHealth():
    response = client.get("/health") #sends GET request to /health endpoint
    assert response.status_code == 200 #verify API responsded successfully
    assert response.json() == {"status": "ok"}

# use this -> 'PYTHONPATH=. pytest' to run tests that treat this directory as an import root