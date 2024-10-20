from fastapi.testclient import TestClient

from app.controller import app

client = TestClient(app)

def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "running"}

def test_predict_sentiment():
    """Test the sentiment prediction endpoint."""
    response = client.post("/predict", json={"text": "I love this product!"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "positive"

def test_empty_text():
    """Test if the API handles empty text input."""
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 400
    assert response.json() == {"detail": "Text input is required."}

