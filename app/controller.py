# app/controller.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
from .model import SentimentModel

app = FastAPI()

# Load the custom-trained model
model = SentimentModel()

# Initialize Hugging Face sentiment analysis pipeline with a 3-class model (positive, negative, neutral)
external_model = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

# Define the request body structure for POST /predict and POST /predict_external
class TextRequest(BaseModel):
    text: str

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "running"}

@app.post("/predict")
def predict_sentiment(request: TextRequest):
    """Predict sentiment using the custom model."""
    if not request.text:
        raise HTTPException(status_code=400, detail="Text input is required.")
    
    # Predict sentiment using the custom-trained model
    sentiment = model.predict_sentiment(request.text)
    return {"sentiment": sentiment}

@app.post("/predict_external")
def predict_sentiment_external(request: TextRequest):
    """Predict sentiment using an external AI API (Hugging Face) for positive, negative, or neutral."""
    if not request.text:
        raise HTTPException(status_code=400, detail="Text input is required.")
    
    # Get the external prediction using Hugging Face model (3-class sentiment analysis)
    external_prediction = external_model(request.text)[0]
    
    # Return the external model's prediction
    return {
        "label": external_prediction["label"],  # 'POSITIVE', 'NEGATIVE', or 'NEUTRAL'
        "score": external_prediction["score"]   # Confidence score
    }
