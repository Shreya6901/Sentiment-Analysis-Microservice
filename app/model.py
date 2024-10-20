# app/model.py
import joblib
import os

class SentimentModel:
    def __init__(self):
        """Loads the sentiment model and the vectorizer from disk."""
        self.model = joblib.load(os.path.join('model', 'sentiment_model.pkl'))
        self.vectorizer = joblib.load(os.path.join('model', 'vectorizer.pkl'))

    def predict_sentiment(self, text: str) -> str:
        """Takes a string input, processes it, and returns a sentiment prediction."""
        # Vectorize the input text
        text_vectorized = self.vectorizer.transform([text])
        # Predict the sentiment using the model
        prediction = self.model.predict(text_vectorized)[0]
        return prediction
